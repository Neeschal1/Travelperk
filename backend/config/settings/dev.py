from .base import *
from env_config import Config

DEBUG = True
ALLOWED_HOST = []


# Database used for Development (db.sqlite3) : For Development Process only
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": Config.ENGINE,
        "NAME": Config.NAME,
        "USER": Config.USER,
        "PASSWORD": Config.PASSWORD,
        "HOST": Config.HOST,
        "PORT": Config.PORT,
    }
}