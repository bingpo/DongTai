# DongTai-core

[![django-project](https://img.shields.io/badge/django%20versions-3.0.3-blue)](https://www.djangoproject.com/)
[![DongTai-project](https://img.shields.io/badge/DongTai%20versions-beta-green)](https://hxsecurity.github.io/DongTaiDoc)
[![DongTai-core](https://img.shields.io/badge/DongTai--core-v1.0-lightgrey)](https://github.com/HXSecurity/dongtai-models)

## 项目介绍
提供DongTai项目依赖的Django Model对象，DongTai项目的Django API抽象类、漏洞检测引擎、常量、文档等内容。

## 快速开始
1. 安装dongtai依赖包

项目打包
```shell script
$ python setup.py sdist
```

安装dongtai包
```shell script
$ pip install dist/dongtai-0.1.0.tar.gz
```

2. 快速开始

在`settings.py`:
```python
INSTALLED_APPS = [
    ...
    'dongtai',
    ...
]
```

3. 打开日志
在`settings.py`中，增加`dongtai-core`的日志loggers及handlers:
```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} [{module}.{funcName}:{lineno}] {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'dongtai.core': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/core.log',
            'backupCount': 5,
            'maxBytes': 1024 * 1024 * 10,
            'formatter': 'verbose'
        },
    },
    'loggers': 
        ...
        'dongtai-core': {
            'handlers': ['console', 'dongtai.core'],
            'propagate': True,
            'level': 'INFO',
        },
        ...
    }
}
```

4. 打开API文档

在`settings.py`引入`drf_yasg`:
```python
INSTALLED_APPS = [
    ...
    'drf_yasg',
    ...
]
```

在`urls.py`中引入`swagger`入口
```python
import os
from django.conf.urls import url
from dongtai.doc import schema_view

urlpatterns = [
    url(r'^doc/$', schema_view(
        title='DongTai OpenAPI',
        version='v1',
        description='DongTai OpenAPI服务接口文档',
        public=True if os.getenv('active.profile', 'PROD') == 'TEST' else False
    ).with_ui('swagger', cache_timeout=None), name='schema-swagger-ui'),
    ...
]
```

在`DjangoView`中增加文档元数据
```python
from dongtai.endpoint import OpenApiEndPoint
from drf_yasg import openapi
from drf_yasg.openapi import Response
from drf_yasg.utils import swagger_auto_schema

from dongtai.endpoint import R


class AgentDownload(OpenApiEndPoint):
    @swagger_auto_schema(
    operation_description="下载Java探针",
    manual_parameters=(
            openapi.Parameter("url", openapi.IN_QUERY, required=True, description="OpenAPI服务器地址",
                              type=openapi.TYPE_STRING),
            openapi.Parameter("projectName", openapi.IN_QUERY, required=True, description="项目名称",
                              type=openapi.TYPE_STRING)
        ),
        responses={200: Response(description='修改成功', examples={'json': {'msg': '修改成功！', "data": []}})},
    )
    def get(self, request):
        return R.success()
```
