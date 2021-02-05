#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:owefsad
# datetime:2021/1/28 上午10:12
# software: PyCharm
# project: lingzhi-engine

from lingzhi_engine.base import R
from vuln.base.method_pool import UserEndPoint
from vuln.models.agent_method_pool import MethodPool
from vuln.serializers.method_pool import MethodPoolSerialize


class MethodPoolEndPoint(UserEndPoint):

    def get(self, request):
        # todo 开放靶场用户的agent数据给每一个用户
        try:
            queryset = MethodPool.objects.filter(agent__in=self.get_auth_agents_with_user(request.user))

            # 根据条件查询
            page = request.query_params.get('page', 1)
            page_size = request.query_params.get('pageSize', 25)
            summary, data = self.get_paginator(queryset=queryset, page=page, page_size=page_size)
            return R.success(data=MethodPoolSerialize(data, many=True).data, page=summary)
        except ValueError as e:
            return R.failure(msg='page和pageSize只能为数字')

    def post(self, request, id):
        return R.success()
