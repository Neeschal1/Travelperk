from .base import *

DEBUG = True
ALLOWED_HOST = []


# Database used for Development (db.sqlite3) : For Development Process only
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}