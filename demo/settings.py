"""
Django settings for demo project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
from corsheaders.defaults import default_headers
from pathlib import Path
import sys
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

sys.path.insert(0, BASE_DIR)
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))
sys.path.insert(0, os.path.join(BASE_DIR, 'utils'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7bvj(zu#fd9d!gc-u%*)6!h&b-lz@5+jw+6d$2)4%-1*u=czv5'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = False

ALLOWED_HOSTS = ['*']

AUTH_USER_MODEL = 'users.UserProfile'

INSTALLED_APPS = [
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'channels',  # 【channels】（第1步）pip install -U channels 安装
    'corsheaders',
    'api.apps.ApiConfig',
    'users.apps.UsersConfig',
    'operation.apps.OperationConfig',
    'order.apps.OrderConfig',
    'message.apps.MessageConfig',
    'barber.apps.BarberConfig',
    'example.apps.ExampleConfig',
    'applets.apps.AppletsConfig',
    'scholl.apps.SchollConfig',
    'upload.apps.UploadConfig',
    'goods.apps.GoodsConfig',
    'system.apps.SystemConfig',
    'store.apps.StoreConfig',
    'fund.apps.FundConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'demo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'demo.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'demo',
        'USER': 'demo',
        'PASSWORD': 'jFAsJixTspBW4Jti',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'OPTIONS': {'charset': 'utf8mb4'},
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# URL尾部不会自动加斜杠
APPEND_SLASH = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = 'static'  # python manage.py collectstatic 收集所有静态文件

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "debug"),
]

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

REST_FRAMEWORK = {
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.IsAdminUser',
    # ],
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # 'PAGE_SIZE': 10
}

REDIS_URL = '159.75.207.157'

# REDIS
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://{REDIS_URL}:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {
                "max_connections": 100
            },
            "PASSWORD": "123456"
        }
    }
}

# django-celery 配置
CELERY_BROKER_URL = f'redis://:123456@{REDIS_URL}:6379/0'  # Broker配置，使用Redis作为消息中间件
CELERY_ACCEPT_CONTENT = ['json']
CELERY_RESULT_BACKEND = f'redis://:123456@{REDIS_URL}:6379/0'  # BACKEND配置，这里使用redis
CELERY_TASK_SERIALIZER = 'json'  # 结果序列化方案
CELERY_TIME_ZONE = 'Asia/Shanghai'
CELERY_ENABLE_UTC = True
CELERY_TASK_TIME_LIMIT = 10

# 跨域配置
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True

# 自定义http标头
CORS_ALLOW_HEADERS = list(default_headers) + [
    'token',
]

HTTP_URL = f'http://{REDIS_URL}:8082'
GIT_ID = 3

# 【channels】（第3步）设置为指向路由对象作为根应用程序
ASGI_APPLICATION = "StarMeow.routing.application"

# 【channels】后端
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [(REDIS_URL, 6379)],
        },
    },
}

try:
    from .local_settings import *
except ImportError:
    pass
