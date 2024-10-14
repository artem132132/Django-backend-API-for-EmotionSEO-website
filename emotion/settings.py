"""
Django settings for emotion project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path
import datetime
from dotenv import load_dotenv 
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$f&8gyq)9ce9ax%23ft*o%&@n17lw)b=(hg_!t9*pmoqafw09r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1','emotionseo.ai', 'www.emotionseo.ai', '51.20.255.29:8000', '51.20.255.29', '0.0.0.0', 'ec2-51-20-255-29.eu-north-1.compute.amazonaws.com', 'ec2-51-20-255-29.eu-north-1.compute.amazonaws.com:8000' ]

CORS_ORIGIN_ALLOW_ALL = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',  #<----
    'user',  #<----
    'corsheaders',
    'rest_framework_simplejwt.token_blacklist',
     'django_rest_passwordreset',
      'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'sslserver',
  
    'rest_framework.authtoken',
    'dj_rest_auth',
]


#SECURE_SSL_REDIRECT = True

#SSL_CERTIFICATE = 'C:\cert\cert.pem'
#SSL_KEY = 'C:\cert\key.pem'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

AUTHENTICATION_BACKENDS = [
   'django.contrib.auth.backends.ModelBackend',
   'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1
STRIPE_PUBLISHABLE_KEY= os.getenv('STRIPE_PUBLISHABLE_KEY')
STRIPE_SECRET_KEY= os.getenv('STRIPE_SECRET_KEY')
STRIPE_PUBLISHABLE_KEY=STRIPE_PUBLISHABLE_KEY
STRIPE_SECRET_KEY =STRIPE_SECRET_KEY
STRIPE_ENDPOINT_SECRET='whsec_b4c044fb0f865b64e5fe682a66688d94fff288c4f44958c57cd0edd1c41d90dd'
STRIPE_PRICE_IDA='price_1OhSurLQgLaib8pXk8bzoqbM'
STRIPE_PRICE_IDB='price_1OhT0cLQgLaib8pXGcDHcNsH'
STRIPE_PRICE_IDC='price_1OhT2ILQgLaib8pXry6DeAs8'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.hostinger.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'hola@emotionseo.ai'
EMAIL_HOST_PASSWORD = '19581958Maria!'

EMAIL_TIMEOUT = 100

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(minutes=1000),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=1),
}

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': ['profile', 'email'],
        'APP': {
            'client_id': '',
            'secret': '',
            'key': ''
        }
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'allauth.account.middleware.AccountMiddleware'
]

ROOT_URLCONF = 'emotion.urls'

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

WSGI_APPLICATION = 'emotion.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_USER_MODEL = "user.User"

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


CORS_ALLOWED_ORIGINS = [
    "https://localhost:3000",
    "https://emotionseo.ai",
    "http://51.20.255.29:3000"
]

BASE_FRONTEND_URL = 'https://emotionseo.ai'
#GOOGLE_OAUTH2_CLIENT_IDKEY= os.getenv('GOOGLE_OAUTH2_CLIENT_IDKEY')
#GOOGLE_OAUTH2_CLIENT_SECRETKEY= os.getenv('GOOGLE_OAUTH2_CLIENT_SECRETKEY')

#GOOGLE_OAUTH2_CLIENT_ID = GOOGLE_OAUTH2_CLIENT_IDKEY
#GOOGLE_OAUTH2_CLIENT_SECRET = GOOGLE_OAUTH2_CLIENT_SECRETKEY