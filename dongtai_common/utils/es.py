from celery import shared_task
from django.apps import apps
from django.db import transaction
from django_elasticsearch_dsl.registries import registry
from django_elasticsearch_dsl.signals import RealTimeSignalProcessor
from django_redis import get_redis_connection
from django.core.cache import cache
from celery.apps.worker import logger
from dongtai_conf.settings import DONGTAI_MAX_RATE_LIMIT
from dongtai_conf.settings import DONGTAI_REDIS_ES_UPDATE_BATCH_SIZE
from dongtai_conf.settings import DONGTAI_MAX_BATCH_TASK_CONCORRENCY
from django_elasticsearch_dsl.registries import registry


@shared_task
def handle_save(pk, app_label, model_name):
    logger.info(f'handle_save to es: {model_name} pk: {pk}')
    sender = apps.get_model(app_label, model_name)
    instance = sender.objects.get(pk=pk)
    registry.update(instance)
    registry.update_related(instance)
    rate_limit_key = f"batch-save-rate-limit-{app_label}-{model_name}-rate_limit"
    cache.decr(rate_limit_key)


@shared_task
def handle_batch_save(app_label, model_name):
    logger.info(f'handle batch save to es: {model_name} app: {app_label}')
    list_key = f"batch-save-list{app_label}-{model_name}-task"
    rate_limit_key = f"batch-save-rate-limit-{app_label}-{model_name}-rate_limit"
    batch_task_count_key = f"batch-save-task-count{app_label}-{model_name}-batch-task-count"
    con = get_redis_connection()
    model_ids = con.lpop(list_key, DONGTAI_REDIS_ES_UPDATE_BATCH_SIZE)
    logger.info(f'handle batch save to es model_ids size: {len(model_ids)}')
    cache.decr(rate_limit_key, len(model_ids))
    for doc in registry._models[model_name]:
        model = doc.Django.model
        model = apps.get_model(app_label, model_name)
        instance_qs = model.objects.filter(pk__in=model_ids).all()
        doc().update(instance_qs)
    listlen = con.llen(list_key)
    if listlen > 0:
        logger.info(listlen)
        handle_batch_save.apply_async(args=(app_label, model_name),
                                      count_down=1)
    else:
        cache.decr(batch_task_count_key)

class DTCelerySignalProcessor(RealTimeSignalProcessor):


    def handle_save(self, sender, instance, **kwargs):
        app_label = instance._meta.app_label
        model_name = instance._meta.model_name

        if instance.__class__ in registry._models or instance.__class__ in registry._related_models:
            rate_limit_key = f"batch-save-rate-limit-{app_label}-{model_name}-rate_limit"
            cache.set(rate_limit_key, 0, nx=True)
            rate_limit = cache.incr(rate_limit_key)
            if rate_limit > DONGTAI_MAX_RATE_LIMIT and instance.__class__ in registry._models:
                logger.info(f'handle_save to es exceed limit : {model_name}')
                transaction.on_commit(
                    lambda: add_task(instance.pk, app_label, model_name))
            else:
                logger.info(f'handle_save to es: {model_name} ')
                transaction.on_commit(lambda: handle_save.delay(
                    instance.pk, app_label, model_name))


def add_task(pk, app_label, model_name):
    list_key = f"batch-save-list{app_label}-{model_name}-task"
    con = get_redis_connection()
    con.rpush(list_key, pk)
    add_async_batch_task(app_label, model_name)


def add_async_batch_task(app_label, model_name):
    batch_task_count_key = f"batch-save-task-count{app_label}-{model_name}-batch-task-count"
    cache.set(batch_task_count_key, 0, nx=True)
    batch_task_count = cache.get(batch_task_count_key)
    if batch_task_count < DONGTAI_MAX_BATCH_TASK_CONCORRENCY:
        cache.incr(batch_task_count_key)
        handle_batch_save.delay(app_label, model_name)
