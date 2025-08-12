from .base import *

DEBUG = True
ALLOWED_HOSTS = ['*']  # dev-safe
INTERNAL_IPS = ['127.0.0.1']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Simpler DB for dev
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

ROOT_URLCONF = "rsite.urls"