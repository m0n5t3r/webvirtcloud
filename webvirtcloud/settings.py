"""
Django settings for webvirtcloud project.

"""

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = False

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']

#AUTHENTICATION_BACKENDS = (
#    'django.contrib.auth.backends.RemoteUserBackend',
#    #'accounts.backends.MyRemoteUserBackend',
#)

LOGIN_URL = '/accounts/login'

ROOT_URLCONF = 'webvirtcloud.urls'

WSGI_APPLICATION = 'webvirtcloud.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
)

## WebVirtCloud settings

# Wobsock port
WS_PORT = 6080

# Websock host
WS_HOST = '0.0.0.0'

# Websock public port
WS_PUBLIC_HOST = None

# Websock SSL connection
WS_CERT = None

# list of console types
QEMU_CONSOLE_TYPES = ['vnc', 'spice']

# default console type
QEMU_CONSOLE_DEFAULT_TYPE = 'vnc'

# list taken from http://qemu.weilnetz.de/qemu-doc.html#sec_005finvocation
QEMU_KEYMAPS = ['ar', 'da', 'de', 'de-ch', 'en-gb', 'en-us', 'es', 'et', 'fi',
                'fo', 'fr', 'fr-be', 'fr-ca', 'fr-ch', 'hr', 'hu', 'is', 'it',
                'ja', 'lt', 'lv', 'mk', 'nl', 'nl-be', 'no', 'pl', 'pt',
                'pt-br', 'ru', 'sl', 'sv', 'th', 'tr']

# keepalive interval and count for libvirt connections
LIBVIRT_KEEPALIVE_INTERVAL = 5
LIBVIRT_KEEPALIVE_COUNT = 5

ALLOW_INSTANCE_MULTIPLE_OWNER = True
CLONE_INSTANCE_DEFAULT_PREFIX = 'ourea'
LOGS_PER_PAGE = 100
QUOTA_DEBUG = True
ALLOW_EMPTY_PASSWORD = True

SECRET_KEY = ''
LOCAL_PATH = None

try:
    from local.local_settings import *  # noqa
except ImportError:
    logging.warning("No local_settings file found.")

# Ensure that we always have a SECRET_KEY set, even when no local_settings.py
# file is present.
# THIS IS A BACKPORT FROM HORIZON https://github.com/openstack/horizon
if not SECRET_KEY:
    if not LOCAL_PATH:
        LOCAL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                  'local')

        from webvirtcloud.utils import secret_key

        SECRET_KEY = secret_key.generate_or_read_from_file(os.path.join(LOCAL_PATH,
                                                           '.secret_key_store'))

# installed apps and middleware shouldn't be overwritten
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'computes',
    'console',
    'networks',
    'storages',
    'interfaces',
    'instances',
    'secrets',
    'logs',
    'accounts',
    'create',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.RemoteUserMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


