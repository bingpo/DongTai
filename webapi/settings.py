"""
Django settings for webapi project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import sys
from configparser import ConfigParser

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import random

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

def ranstr(num):
    H = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()`-{}|:?><>?'
    salt = ''
    for i in range(num):
        salt += random.choice(H)
    return salt


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ranstr(50)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("debug", 'false') == 'true'

# READ CONFIG FILE
config = ConfigParser()
status = config.read(os.path.join(BASE_DIR, 'conf/config.ini'))
if len(status) == 0:
    print("config file not exist. stop running")
    exit(0)

# DEBUG = True
ALLOWED_HOSTS = ['*']

# Application definition
TOKEN_EXP_DAY = 14

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',
    'corsheaders',
    'captcha',
    'dongtai',
    'iast',
    'modeltranslation',
]
MODELTRANSLATION_LANGUAGES = ('en', 'zh')
REST_FRAMEWORK = {
    'PAGE_SIZE':
        20,
    'DEFAULT_PAGINATION_CLASS': ['django.core.paginator'],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_THROTTLE_CLASSES': ('rest_framework.throttling.AnonRateThrottle',
                                 'rest_framework.throttling.UserRateThrottle'),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '1000/min',
        'user': '5000/min'
    },
}

basedir = os.path.dirname(os.path.realpath(__file__))
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'i18n'),
)
LANGUAGE_CODE = 'zh'
LANGUAGES = (
    ('en', 'English'),
    ('zh', '简体中文'),
)
USE_I18N = True
USE_L10N = True

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'xff.middleware.XForwardedForMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

XFF_TRUSTED_PROXY_DEPTH = 5

CSRF_COOKIE_NAME = "DTCsrfToken"
CSRF_HEADER_NAME = "HTTP_CSRF_TOKEN"
# CSRF_COOKIE_DOMAIN = ".huoxian.cn"
CSRF_TRUSTED_ORIGINS = (
    ".huoxian.cn:8000",
    ".huoxian.cn:8001",
    ".huoxian.cn",
    ".secnium.xyz"
    ".secnium.xyz:8000"
    ".secnium.xyz:8001"
)
CSRF_COOKIE_AGE = 60 * 60 * 24

AGENT_UPGRADE_URL = "https://www.huoxian.cn"


CORS_ORIGIN_REGEX_WHITELIST = [
    r"^https://\w+\.huoxian.cn:(\:\d+)?$"
]

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_METHODS = [
    'GET',
    'OPTIONS',
    'POST',
]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'referer',
    'x-token',
    'user-agent',
    'x-csrftoken',
    'csrf-token',
    'x-requested-with',
]

ROOT_URLCONF = 'webapi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'webapi.wsgi.application'

if 0 and len(sys.argv) > 1 and sys.argv[1] in ('test', 'makemigrations',
                                         'sqlmigrate','migrate'):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'OPTIONS': {
                'charset': 'utf8mb4'
            },
            'USER': config.get("mysql", 'user'),
            'NAME': config.get("mysql", 'name'),
            'PASSWORD': config.get("mysql", 'password'),
            'HOST': config.get("mysql", 'host'),
            'PORT': config.get("mysql", 'port'),
            'OPTIONS': {
                'init_command': 'SET max_execution_time=20000'
            },
        }
    }

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 6,
        }
    },
]
AUTH_USER_MODEL = 'dongtai.User'

LANGUAGE_CODE = 'zh'

TIME_ZONE = "Asia/Shanghai"

USE_I18N = True

USE_L10N = True

STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'iast', 'upload')
MEDIA_URL = "/upload/masterimg/"


CAPTCHA_IMAGE_SIZE = (80, 45)
CAPTCHA_LENGTH = 4
CAPTCHA_TIMEOUT = 1

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} [{module}.{funcName}:{lineno}] {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'dongtai-webapi': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/dongtai-webapi.log'),
            'backupCount': 5,
            'maxBytes': 1024 * 1024 * 10,
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'dongtai-webapi': {
            'handlers': ['console', 'dongtai-webapi'],
            'propagate': True,
            'level': 'INFO',
        },
    }
}

REST_PROXY = {
    'HOST': config.get("engine", 'url'),
}


# notify
EMAIL_SERVER = config.get('smtp', 'server')
EMAIL_USER = config.get('smtp', 'user')
EMAIL_PASSWORD = config.get('smtp', 'password')
EMAIL_FROM_ADDR = config.get('smtp', 'from_addr')
ENABLE_SSL = config.get('smtp', 'ssl') == 'True'
ADMIN_EMAIL = config.get('smtp', 'cc_addr')
SESSION_COOKIE_DOMAIN = None
CSRF_COOKIE_DOMAIN = None
if os.getenv('environment', 'PROD') == 'TEST':
    INSTALLED_APPS.append('drf_spectacular')
    SPECTACULAR_SETTINGS = {
        'TITLE': 'DongTai webapi',
    }
    REST_FRAMEWORK[
        'DEFAULT_SCHEMA_CLASS'] = 'drf_spectacular.openapi.AutoSchema'
if os.getenv('environment', None) in ('TEST', 'PROD'):
    SESSION_COOKIE_DOMAIN = config.get('other',
                                            'demo_session_cookie_domain')
    CSRF_COOKIE_DOMAIN = SESSION_COOKIE_DOMAIN
    DOMAIN = config.get('other', 'domain')
