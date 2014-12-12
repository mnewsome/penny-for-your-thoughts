import os
from os import environ as env
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = env.get('SECRET_KEY')

#DEBUG = True if env.get('DEBUG', True) == True else False
DEBUG = True

TEMPLATE_DEBUG = True

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'thoughts',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "penny_for_your_thoughts/templates"),
)

ROOT_URLCONF = 'penny_for_your_thoughts.urls'

WSGI_APPLICATION = 'penny_for_your_thoughts.wsgi.application'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SHELL_PLUS = 'ipython'

# Celery settings
BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

import dj_database_url
DATABASES = {'default': dj_database_url.config()}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
        )
