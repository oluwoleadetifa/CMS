from .settings import *

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'NAME': 'admin',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'admin',
        'PASSWORD': 'admin123'
    }
}