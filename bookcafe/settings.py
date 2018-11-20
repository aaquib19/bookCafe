"""
Django settings for bookcafe project.

Generated by 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v(x@((pxe#s#&#2u&pgop%#n*zp5129_7agiefeh*s#caoh!=n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'cronta',               #handling email sending
    'django_crontab',       #handling cron jobs add,remove,show
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #USER INSTALLED APPS
    'book',
    'accounts',
    'search',
    'category',
    #'tok',
    'borrower',
    'donation',

    'crispy_forms',
    'notification',

]

AUTH_USER_MODEL = 'accounts.user'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

LOGOUT_REDIRECT_URL = '/login/'
ROOT_URLCONF = 'bookcafe.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'bookcafe.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}




# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static_')

#AUTH_USER_MODEL = 'acounts.User'

LOGIN_URL = '/accounts/login/'

LOGOUT_URL = '/accounts/logout/'

LOGIN_REDIRECT_URL = 'home'

LOGOUT_REDIRECT_URL = 'home'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]


MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media_')

#to handle email and cron processes
#just define cron process in CRONJOBS and run command python manage.py crotab add and to remove use remove insteat of add
CRONJOBS = [
    ('*/1 * * * *','cronta.cron.my_jobs'),
    ('*/1 * * * *','notification.cron.TokenExpire'),
]

# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'info.educardo@gmail.com'
# DEFAULT_FROM_EMAIL = 'info.educardo@gmail.com'
# DEFAULT_REPLYTO_EMAIL = 'info.educardo@gmail.com'
# EMAIL_HOST_PASSWORD = '*********'
# EMAIL_PORT = 587
#

import smtplib
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
smtp=smtplib.SMTP(host=EMAIL_HOST,port=EMAIL_PORT)

EMAIL_USE_TLS = True
# EMAIL_HOST = 'smpt.gmail.com'
EMAIL_HOST_USER = 'rehanmallick4080@gmail.com'
EMAIL_HOST_PASSWORD = 'iamalilwayne'
# EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'rehanmallick4080@gmail.com'

# ADMINS = (
#     ('You', 'you@email.com'),
# )
# MANAGERS = ADMINS