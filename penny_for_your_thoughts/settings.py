import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ENV = os.environ

SECRET_KEY = ENV.get('SECRET_KEY')

DEBUG = True if ENV.get('DEBUG') == 'True' else False

STRIPE_SECRET_KEY = ENV.get('STRIPE_TEST_SECRET_KEY') if DEBUG == True else ENV.get('STRIPE_LIVE_SECRET_KEY')
STRIPE_PUBLISHABLE_KEY = ENV.get('STRIPE_TEST_PUBLISHABLE_KEY') if DEBUG == True else ENV.get('STRIPE_LIVE_PUBLISHABLE_KEY')

REDIS_HOST = ENV.get('REDIS_DEV_HOST') if DEBUG == True else ENV.get('REDIS_PROD_HOST')
REDIS_PORT = ENV.get('REDIS_DEV_PORT') if DEBUG == True else ENV.get('REDIS_PROD_PORT')
REDIS_DB   = ENV.get('REDIS_DEV_DB') if DEBUG == True else ENV.get('REDIS_PROD_DB')

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
    'payments',
    'accounts',
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

TIME_ZONE = 'America/Chicago'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SHELL_PLUS = 'ipython'

# Celery settings
BROKER_URL = 'redis://127.0.0.1:6379/0'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'

import dj_database_url
DATABASES = {'default': dj_database_url.config()}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'

STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
        )
