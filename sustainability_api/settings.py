from pathlib import Path
from datetime import timedelta
from decouple import config
import pymysql
pymysql.install_as_MySQLdb()
import os
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY= config('SECRET_KEY')
DEBUG = True

ALLOWED_HOSTS = ['*']

BASE_DIR = Path(__file__).resolve().parent.parent

#define a folder conating media or picture content
MEDIA_URL='/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')



INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'rest_framework',
    'corsheaders',
    'api',
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "sustainability_api.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = "sustainability_api.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

ENV = str(config('ENV', 'development')).lower()

if ENV == 'development':
    # take sql lite db
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    # take postgres db
    DATABASES = {
        "default": {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': config('MYSQL_DATABASE', 'postgres'),
            'USER': config('MYSQL_USER', 'postgres'),
            'PASSWORD': config('MYSQL_PASSWORD', ''),
            'HOST': config('MYSQL_HOST', 'localhost'),
            'PORT': config('MYSQL_PORT', '3306'),
        }
    }



# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

#CORS settings
CORS_ALLOW_ALL_ORIGINS = True

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Dar_es_Salaam'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# handling static files
USE_S3 = config('USE_S3')
if USE_S3 == 'YES':
    
    # aws settings
    AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
    AWS_END_POINT = config('AWS_END_POINT')
    AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
    AWS_DEFAULT_ACL = None
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.{AWS_END_POINT}'
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=172800'}
    
   # s3 static settings
    STATIC_LOCATION = 'static'
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
    STATICFILES_STORAGE = 'storage_backends.StaticStorage'
    
    # s3 public media settings
    PUBLIC_MEDIA_LOCATION = 'media'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'
    DEFAULT_FILE_STORAGE = 'storage_backends.PublicMediaStorage'

else:
    STATIC_URL = '/static/'
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
    STATIC_ROOT = BASE_DIR / "staticfiles"
    MEDIA_URL = '/media/'
    MEDIA_ROOT =  BASE_DIR / 'media'
    

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 50

}

if config("ALLOW_LOCALHOST") == "YES":
    CORS_ALLOWED_ORIGIN_REGEXES = [
        r"^https://\w+\.safaripro\.net$",
        r"^https://\w+\.safaripro\.co\.tz$",
        "*",
    ]
else:
    CORS_ALLOWED_ORIGIN_REGEXES = [
        r"^https://\w+\.safaripro\.net$",
        r"^https://\w+\.safaripro\.co\.tz$",
    ]


CORS_ALLOW_ALL_ORIGINS = False

if config("ALLOW_LOCALHOST") == "YES":
    CSRF_TRUSTED_ORIGINS = [
        """ Allow all subdomains of safaripro.co.tz """
        r"^https://\w+\.safaripro\.net$",
        r"^https://\w+\.safaripro\.co\.tz$",
        "*",
    ]
else:
    CSRF_TRUSTED_ORIGINS = [
        """ Allow all subdomains of safaripro.co.tz """
        r"^https://\w+\.safaripro\.net$",
        r"^https://\w+\.safaripro\.co\.tz$",
    ]
