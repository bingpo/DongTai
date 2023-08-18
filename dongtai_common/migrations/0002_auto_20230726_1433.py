# Generated by Django 3.2.20 on 2023-07-26 14:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import dongtai_common.utils.db


def add_preset_admin_role(apps, schema_editor):
    from dongtai_common.models.iast_role import IastRoleV2, RoleStatus

    IastRoleV2.objects.create(
        name="管理员",
        is_admin=True,
        is_preset=True,
        permission={
            "routes": [
                "links",
                "project",
                "projectManage",
                "vulnList",
                "scanList",
                "scaList",
                "agentManage",
                "deployment",
                "environment",
                "deploy",
                "integrationManagement",
                "strategyBox",
                "strategyManage",
                "templateManage",
                "hookRule",
                "sensitiveManage",
                "projectTemplate",
                "systemSettings",
                "search",
                "center",
                "reportCenter",
                "vulnSharing",
                "license",
                "changeLogo",
                "logManage",
                "about",
                "knowledge",
                "authority",
                "roleSetting",
                "team",
                "account",
                "dashboard",
                "Dashboard",
            ],
            "buttons": [
                {"label": "新增项目", "id": 1},
                {"label": "删除项目", "id": 2},
                {"label": "编辑项目", "id": 3},
                {"label": "生成报告", "id": 4},
                {"label": "删除漏洞", "id": 5},
                {"label": "关联漏洞", "id": 6},
                {"label": "漏洞分享", "id": 7},
                {"label": "状态变更", "id": 8},
                {"label": "集成同步", "id": 9},
                {"label": "组件分享", "id": 10},
                {"label": "启用", "id": 11},
                {"label": "暂停", "id": 12},
                {"label": "导出日志", "id": 13},
                {"label": "批量升级", "id": 14},
                {"label": "主动验证", "id": 15},
                {"label": "熔断配置", "id": 16},
                {"label": "IDE 插件", "id": 17},
                {"label": "CI/CD 集成", "id": 18},
                {"label": "缺陷管理", "id": 19},
                {"label": "消息通知", "id": 20},
                {"label": "其他", "id": 21},
                {"label": "新增策略", "id": 22},
                {"label": "编辑策略", "id": 23},
                {"label": "删除策略", "id": 24},
                {"label": "修改状态", "id": 25},
                {"label": "新增模版", "id": 26},
                {"label": "编辑模版", "id": 27},
                {"label": "删除模版", "id": 28},
                {"label": "修改状态", "id": 29},
                {"label": "添加规则类型", "id": 30},
                {"label": "添加规则", "id": 31},
                {"label": "删除规则", "id": 32},
                {"label": "修改状态", "id": 33},
                {"label": "全部启用", "id": 34},
                {"label": "全部禁用", "id": 35},
                {"label": "全部删除", "id": 36},
                {"label": "新增规则", "id": 37},
                {"label": "编辑规则", "id": 38},
                {"label": "删除规则", "id": 39},
                {"label": "修改状态", "id": 40},
                {"label": "新增配置", "id": 41},
                {"label": "编辑模版", "id": 42},
                {"label": "只读", "id": 43},
                {"label": "修改", "id": 44},
                {"label": "新增角色", "id": 45},
                {"label": "删除角色", "id": 46},
                {"label": "编辑角色", "id": 47},
                {"label": "新增项目组", "id": 48},
                {"label": "删除项目组", "id": 49},
                {"label": "编辑项目组", "id": 50},
                {"label": "查看详情", "id": 51},
                {"label": "新增账号", "id": 52},
                {"label": "删除账号", "id": 53},
                {"label": "编辑账号", "id": 54},
                {"label": "查看详情", "id": 55},
                {"label": "消息通知", "id": 56},
                {"label": "删除模版", "id": 57},
            ],
        },
        status=RoleStatus.ENABLE,
    )
    IastRoleV2.objects.create(
        name="普通成员",
        is_admin=True,
        is_preset=True,
        permission={
            "routes": [
                "links",
                "project",
                "projectManage",
                "vulnList",
                "scanList",
                "scaList",
                "agentManage",
                "deployment",
                "environment",
                "deploy",
                "integrationManagement",
                "strategyBox",
                "strategyManage",
                "templateManage",
                "hookRule",
                "sensitiveManage",
                "projectTemplate",
                "systemSettings",
                "search",
                "center",
                "reportCenter",
                "vulnSharing",
                "license",
                "changeLogo",
                "logManage",
                "about",
                "knowledge",
                "authority",
                "dashboard",
                "Dashboard",
            ],
            "buttons": [
                {"label": "新增项目", "id": 1},
                {"label": "删除项目", "id": 2},
                {"label": "编辑项目", "id": 3},
                {"label": "生成报告", "id": 4},
                {"label": "删除漏洞", "id": 5},
                {"label": "关联漏洞", "id": 6},
                {"label": "漏洞分享", "id": 7},
                {"label": "状态变更", "id": 8},
                {"label": "集成同步", "id": 9},
                {"label": "组件分享", "id": 10},
                {"label": "启用", "id": 11},
                {"label": "暂停", "id": 12},
                {"label": "导出日志", "id": 13},
                {"label": "批量升级", "id": 14},
                {"label": "主动验证", "id": 15},
                {"label": "熔断配置", "id": 16},
                {"label": "IDE 插件", "id": 17},
                {"label": "CI/CD 集成", "id": 18},
                {"label": "缺陷管理", "id": 19},
                {"label": "消息通知", "id": 20},
                {"label": "其他", "id": 21},
                {"label": "新增策略", "id": 22},
                {"label": "编辑策略", "id": 23},
                {"label": "删除策略", "id": 24},
                {"label": "修改状态", "id": 25},
                {"label": "新增模版", "id": 26},
                {"label": "编辑模版", "id": 27},
                {"label": "删除模版", "id": 28},
                {"label": "修改状态", "id": 29},
                {"label": "添加规则类型", "id": 30},
                {"label": "添加规则", "id": 31},
                {"label": "删除规则", "id": 32},
                {"label": "修改状态", "id": 33},
                {"label": "全部启用", "id": 34},
                {"label": "全部禁用", "id": 35},
                {"label": "全部删除", "id": 36},
                {"label": "新增规则", "id": 37},
                {"label": "编辑规则", "id": 38},
                {"label": "删除规则", "id": 39},
                {"label": "修改状态", "id": 40},
                {"label": "新增配置", "id": 41},
                {"label": "编辑模版", "id": 42},
                {"label": "只读", "id": 43},
                {"label": "修改", "id": 44},
                {"label": "消息通知", "id": 56},
                {"label": "删除模版", "id": 57},
            ],
        },
        status=RoleStatus.ENABLE,
    )


class Migration(migrations.Migration):
    dependencies = [
        ("dongtai_common", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="IastProjectGroup",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                ("create_time", models.IntegerField(default=dongtai_common.utils.db.get_timestamp)),
            ],
            options={
                "db_table": "iast_project_group",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="IastRole",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                ("is_admin", models.BooleanField(default=False)),
                ("is_preset", models.BooleanField(default=False)),
                ("permission", models.JSONField()),
                ("status", models.IntegerField(choices=[(0, "禁用"), (1, "启用")])),
            ],
            options={
                "db_table": "iast_role",
                "managed": True,
            },
        ),
        migrations.AddField(
            model_name="user",
            name="is_global_permission",
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name="IastProjectUser",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "project",
                    models.ForeignKey(
                        db_constraint=False,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="dongtai_common.iastproject",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
            options={
                "db_table": "iast_project_user",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="IastProjectGroupUser",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "project_group",
                    models.ForeignKey(
                        db_constraint=False,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="dongtai_common.iastprojectgroup",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
            options={
                "db_table": "iast_project_group_user",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="IastProjectGroupProject",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "project",
                    models.ForeignKey(
                        db_constraint=False,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="dongtai_common.iastproject",
                    ),
                ),
                (
                    "project_group",
                    models.ForeignKey(
                        db_constraint=False,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="dongtai_common.iastprojectgroup",
                    ),
                ),
            ],
            options={
                "db_table": "iast_project_group_project",
                "managed": True,
            },
        ),
        migrations.AddField(
            model_name="iastprojectgroup",
            name="create_user",
            field=models.ForeignKey(
                db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="role",
            field=models.ForeignKey(
                db_constraint=False,
                default=1,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="dongtai_common.iastrole",
            ),
        ),
        migrations.RunPython(add_preset_admin_role),
    ]