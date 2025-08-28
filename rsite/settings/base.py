import os
from pathlib import Path
from decouple import config, Csv

BASE_DIR = Path(__file__).resolve().parent.parent.parent
TEST_RUNNER = 'django.test.runner.DiscoverRunner'

SECRET_KEY = config('DJANGO_SECRET_KEY', default='unsafe-default-key')
DEBUG = config('DJANGO_DEBUG', default=False, cast=bool)

raw_hosts = config('DJANGO_ALLOWED_HOSTS', default='localhost', cast=Csv())
# ALLOWED_HOSTS = raw_hosts if isinstance(raw_hosts, (list, tuple)) else [raw_hosts]
ALLOWED_HOSTS = ["localhost", "rsite.local", "127.0.0.1"]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # custom apps
    'abode',
    
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

ROOT_URLCONF = 'rsite.urls'
WSGI_APPLICATION = 'rsite.wsgi.application'

LANGUAGE_CODE = config('LANGUAGE_CODE', default='en-us')
TIME_ZONE = config('TIME_ZONE', default='UTC')

STATIC_URL = config('STATIC_URL')
MEDIA_URL = config('MEDIA_URL')
STATIC_ROOT = config('STATIC_ROOT', default=os.path.join(BASE_DIR, 'staticfiles'))
MEDIA_ROOT = config('MEDIA_ROOT', default=os.path.join(BASE_DIR, 'mediafiles'))

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {'min_length': 8},
    },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'