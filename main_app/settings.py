"""
Django settings for dj3 project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-n^-yycjnisrp2mr@!0-%7k^vu&1%pqacng4w(=8g9)k8u$a29@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dj3.urls'

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

WSGI_APPLICATION = 'dj3.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ROOT_URLCONF = 'main_app.urls'
WSGI_APPLICATION = 'main_app.wsgi.application'
SITE_ID = 1
import os
import json
from shutil import copyfile

STATIC_ROOT = os.path.join(BASE_DIR, "static/")
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
#SESSION_COOKIE_AGE = 3600

config_path = (str(BASE_DIR)+'/config.json')
config_path = config_path.replace('\\/', '\\')
config_path = config_path.replace('//', '/')
if not os.path.exists(config_path):
    temp_path = config_path.replace('config.json', 'example.config.json')
    copyfile(temp_path, config_path)


LOCALHOST = False
SITE_URL = 'http://localhost:8000'

with open(config_path, 'r') as site_config:
    config_info = json.load(site_config)
    env_type = config_info.get('env')
    if config_info.get('local'):
        LOCALHOST = True
        ALLOWED_HOSTS = ['*']
    if env_type == 'dev':
        DEBUG = True
    else:
        ALLOWED_HOSTS = ALLOWED_HOSTS
        DEBUG = False
    active_db = config_info.get('active_db')
    if active_db:
        db_config = config_info.get(active_db)
        if db_config:
            DATABASES['default'] = config_info[active_db]
    SITE_NAME = config_info.get('site_name')
    SITE_URL = config_info.get('site_url')

rest_apps = ["rest_framework", "rest_framework.authtoken"]
util_apps = ['sorter', 'pusher', 'sam_dj_tinymce']
project_apps = ['news']
base_apps = ['website']
INSTALLED_APPS = base_apps + INSTALLED_APPS
ALLOW_UNICODE_SLUGS = True

LOGIN_URL = '/admin/login/'

MIDDLEWARE = MIDDLEWARE + [
    'website.middleware.TimezoneMiddleware',
    'website.response_handler.ExceptionMiddleware'
]
# REST_FRAMEWORK = {
#     "DEFAULT_AUTHENTICATION_CLASSES": (
#         "rest_framework.authentication.TokenAuthentication",
#         "rest_framework.authentication.SessionAuthentication",
#     ),
#     "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
# }
