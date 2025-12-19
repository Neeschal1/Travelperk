from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent.parent
from env_config import Config
from datetime import timedelta

# Secret Key
SECRET_KEY = Config.SECRET_KEY


# Application Definitions
INSTALLED_APPS = [
    # Cors Header
    'corsheaders',
    
    # Default
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Packages
    'rest_framework',
    'drf_yasg',
    
    # Apps
    'rest_framework_simplejwt',
    'apps.accounts',
    'apps.cars',
    'apps.cuisines',
    'apps.flights',
    'apps.hotel',
    'apps.payments',
    'apps.touristguide',
    'apps.travel_destinations',
    'apps.ai_assistant',
    'apps.bookings',
    'apps.verifications',
]


# Middlewares
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# Root URL Configurations
ROOT_URLCONF = 'config.urls'


# Templates Involved
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# Web Server Gunicorn Interface
WSGI_APPLICATION = 'config.wsgi.application'


# Rest Frameworks Dependencies
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}


# Password Validations
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]


# SimpleJWT Setup
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME' : timedelta(minutes=15),
    'REFRESH_TOKEN_LIFETIME' : timedelta(days=7),
    'AUTH_HEADER_TYPES' : ('Bearer', )
}


# Internationalizations
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Static files
STATIC_URL = 'static/'