from pathlib import Path
from datetime import timedelta
from django.conf.global_settings import AUTH_USER_MODEL
from Apps.Catalogos.setting_apps import Catalogos_Settings_Apps
from Apps.Operaciones.setting_apps import Operaciones_Settings_Apps
from Apps.Seguridad.setting_apps import Seguridad_Settings_Apps
from Apps.Dashboard.setting_apps import Dashboard_Settings_Apps

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-_f(&%@grcg!b9#96ol!&6tt2t$%0r9hldb2e9@(q^ebd7k&bvz'

# DEBUG = True
# ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'corsheaders',  # ✅ Importante para permitir CORS
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_filters',
    'drf_yasg',
    'rest_framework_simplejwt',
] + Seguridad_Settings_Apps + Catalogos_Settings_Apps + Operaciones_Settings_Apps + Dashboard_Settings_Apps

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',               # ✅ Debe ir antes que CommonMiddleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'config.middleware.DebugRequestMiddleware',
]

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'

# DATABASES configurado desde otro archivo o manualmente

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        # Puedes comentar esto si no usas permisos globales
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
}

LANGUAGE_CODE = 'es-Ni'
TIME_ZONE = 'America/Managua'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'Usuarios.User'

# ✅ CONFIGURACIÓN CORS PARA PERMITIR EL FRONTEND LOCAL
CORS_ALLOWED_ORIGINS = [
    "http://localhost:63342",
    "http://127.0.0.1:63342",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:5500",  # ✅ Donde estás corriendo tu HTML
    "http://localhost:5500"
]

# Alternativa si quieres permitir todo (solo para desarrollo)
# CORS_ALLOW_ALL_ORIGINS = True
