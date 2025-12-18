from .base import *

DEBUG = False
ALLOWED_HOSTS = []

# Default Database (Postgre SQL) : For production
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "Travelperk",
        "USER": "neondb_owner",
        "PASSWORD": "npg_Xi1jDaLlhtB5",
        "HOST": "ep-mute-sunset-a13tzyhd-pooler.ap-southeast-1.aws.neon.tech",
        "PORT": "5432",
    }
}
