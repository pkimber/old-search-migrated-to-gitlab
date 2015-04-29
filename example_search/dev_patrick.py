# -*- encoding: utf-8 -*-
from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'temp.db',                               # Or path to database file if using sqlite3.
        'USER': '',                               # Not used with sqlite3.
        'PASSWORD': '',                           # Not used with sqlite3.
        'HOST': '',                              # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                                          # Set to empty string for default. Not used with sqlite3.
    }
}

# simple engine (dev only)
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}

#HAYSTACK_CONNECTIONS = {
#    'default': {
#        'BATCH_SIZE': 100,
#        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
#        'INDEX_NAME': 'example_search',
#        'TIMEOUT': 60 * 5,
#        'URL': 'http://127.0.0.1:9200/',
#    },
#}
