"""
Django settings for twistedexample project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os


def _env(variable, default=None):
    return os.environ.get(variable, default)


def _env_bool(variable, default=None):
    if _env(variable, default) == 'true':
        return True
    elif _env(variable, default) == 'false':
        return False
    else:
        return default

ENVIRONMENT = _env('ENVIRONMENT')

if not ENVIRONMENT:
    raise Exception('No environment selected')


BASE_DIR = os.path.dirname(__file__)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'rjgs6=#t#g!b)vfrp9twv+nel9v0=5pzmnnnkmn&-269$7t1w2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = _env_bool('DEBUG', False)


ALLOWED_HOSTS = _env('ALLOWED_HOSTS').split() if _env('ALLOWED_HOSTS') else []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'crm',
    'mailing',
    'workspace',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'crm', 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'debug': DEBUG,
        },
    },
]

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': _env('DATABASE_ENGINE'),
        'NAME': _env('DATABASE_NAME'),
        'USER': _env('DATABASE_USER'),
        'PASSWORD': _env('DATABASE_PASSWORD'),
        'HOST': _env('DATABASE_HOST'),
        'PORT': _env('DATABASE_PORT'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static', 'static')

MEDIA_URL = '/static/uploads/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static', 'uploads')
