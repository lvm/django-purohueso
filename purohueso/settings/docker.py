# pylint: skip-file
import os
from .common import *

SECRET_KEY = 'GmEeCNnwGwa91jmXlISTFjgjVxREL3bsAs6hpd4ZnLmFOPTFtj'

DEBUG = True

ENV_NAME = 'Docker'

MEDIA_ROOT = '/tmp/purohueso-api-media'
STATIC_ROOT = '/tmp/purohueso-api'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT')
    }
}

