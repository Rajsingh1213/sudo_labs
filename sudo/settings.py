import os
from pathlib import Path
from datetime import timedelta

# BASE_DIR points to the project root
BASE_DIR = Path(__file__).resolve().parent.parent


# ---------------------
# SECURITY SETTINGS
# ---------------------

# SECURITY WARNING: keep the secret key secret in production! Use env vars.
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'your-development-secret-key')

# DEBUG mode should be False in production!
DEBUG = os.getenv('DJANGO_DEBUG', 'True').lower() in ('true', '1')

# Set allowed hosts, e.g. your domain or IP addresses
ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', 'localhost 127.0.0.1').split()


# ---------------------
# APPLICATION DEFINITION
# ---------------------

INSTALLED_APPS = [
    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party apps
    'rest_framework',
    'corsheaders',
    'ckeditor',

    # Your apps
    'backend',  # Replace with your app name
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # if using CORS
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sudo.urls'  # Replace with your project name


# ---------------------
# TEMPLATES
# ---------------------

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # your templates folder
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # needed for DRF browsable API
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'sudo.wsgi.application'  # Replace with your project name


# ---------------------
# DATABASE
# ---------------------

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DJANGO_DB_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': os.getenv('DJANGO_DB_NAME', BASE_DIR / 'db.sqlite3'),
        'USER': os.getenv('DJANGO_DB_USER', ''),
        'PASSWORD': os.getenv('DJANGO_DB_PASSWORD', ''),
        'HOST': os.getenv('DJANGO_DB_HOST', ''),
        'PORT': os.getenv('DJANGO_DB_PORT', ''),
    }
}


# ---------------------
# PASSWORD VALIDATION
# ---------------------

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {'min_length': 8},
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# ---------------------
# INTERNATIONALIZATION
# ---------------------

LANGUAGE_CODE = 'en-us'

TIME_ZONE = os.getenv('DJANGO_TIME_ZONE', 'Asia/Kolkata')

USE_I18N = True
USE_L10N = True
USE_TZ = True


# ---------------------
# STATIC & MEDIA FILES
# ---------------------

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Run collectstatic to populate this in production

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# ---------------------
# DJANGO REST FRAMEWORK
# ---------------------

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',  # Change to IsAuthenticated in prod
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        # For token auth add:
        # 'rest_framework.authentication.TokenAuthentication',
        # For JWT add:
        # 'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',  # Fast JSON responses
        'rest_framework.renderers.BrowsableAPIRenderer',  # Optional: browsable API in dev
    ],
}


# ---------------------
# CORS (if frontend calls backend API from different domain)
# ---------------------

CORS_ALLOWED_ORIGINS = os.getenv('DJANGO_CORS_ALLOWED_ORIGINS', '').split()
# Example: 'http://localhost:3000'

# To allow all (not recommended in production)
# CORS_ALLOW_ALL_ORIGINS = True


# ---------------------
# DEFAULT AUTO FIELD
# ---------------------

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ---------------------
# SECURITY HARDENING (Production settings example)
# ---------------------

if not DEBUG:
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = True
    SECURE_HSTS_SECONDS = 3600
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_REFERRER_POLICY = 'no-referrer-when-downgrade'
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True