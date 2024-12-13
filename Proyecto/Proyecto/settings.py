import os
from pathlib import Path

# Ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Seguridad
SECRET_KEY = 'tu_clave_secreta_aqui'  # Cambia esto por tu clave secreta

# Modo de depuración
DEBUG = True  # Cambia a False en producción

ALLOWED_HOSTS = []  # Agrega los hosts permitidos en producción

# Aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'App',  # Tu aplicación
    'accounts',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configuración de URL
ROOT_URLCONF = 'Proyecto.urls'

# Plantillas
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',  # Asegúrate de que esta ruta esté correcta
        ],
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


# WSGI
WSGI_APPLICATION = 'Proyecto.wsgi.application'

# Configuración de la base de datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Cambia esto si usas otro sistema de base de datos
        'NAME': BASE_DIR / 'db.sqlite3',  # Cambia esto si usas otro nombre o ubicación
    }
}

# Autenticación
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

# Configuración internacional
LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Archivos estáticos
STATIC_URL = '/static/'

# Agregar la ruta a los archivos estáticos de tu aplicación
STATICFILES_DIRS = [
    BASE_DIR / 'static',
    BASE_DIR / 'accounts/static',  # Si tienes una carpeta static dentro de la app 'accounts'
]

# Archivos multimedia (para subir imágenes u otros archivos)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'App/media'

# Configuración de la seguridad
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = False  # Cambia a True en producción si usas HTTPS
SESSION_COOKIE_SECURE = False  # Cambia a True en producción si usas HTTPS
CSRF_COOKIE_SECURE = False  # Cambia a True en producción si usas HTTPS

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/accounts/login/'
