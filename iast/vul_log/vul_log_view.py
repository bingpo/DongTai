from dongtai.models.iast_vul_log import (IastVulLog, MessageTypeChoices)
from dongtai.utils import const
from dongtai.models.hook_type import HookType
from dongtai.models.strategy import IastStrategyModel
from dongtai.models.document import IastDocument

from dongtai.endpoint import R
from dongtai.utils import const
from dongtai.endpoint import UserEndPoint
from django.forms.models import model_to_dict
from django.db.models import Q
from rest_framework import serializers
from rest_framework.serializers import ValidationError
from iast.utils import extend_schema_with_envcheck, get_response_serializer
from django.utils.translation import gettext_lazy as _
from rest_framework import viewsets
from iast.common import VulType

class VulLogViewSet(UserEndPoint, viewsets.ViewSet):
    name = "api-v1-vul-log"
    description = _("vul-log")

    def list(self, request, vul_id):
        data = []
        auth_users = self.get_auth_users(request.user)
        vul_type = VulType(int(request.query_params.get('vul_type', 1)))
        if vul_type == VulType.APPLICATION:
            data = IastVulLog.objects.filter(vul_id=vul_id,
                                             user__in=auth_users).all()
        if vul_type == VulType.ASSET:
            data = IastVulLog.objects.filter(asset_vul_id=vul_id,
                                             user__in=auth_users).all()

        return R.success([model_to_dict(i) for i in data])
