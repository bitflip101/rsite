from .base import *

DEBUG = True

# Disable these for local HTTP testing
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

# The rest of your local-specific settings can go here
ALLOWED_HOSTS = ['*']