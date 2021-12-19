from decouple import config
import sys
import os
from .settings import BASE_DIR

database_name = config('DATABASE_NAME')
database_host = config('DATABASE_HOST')

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': database_name,
        'CLIENT': {
            'host': database_host,
        }
    }
}

if 'test' in sys.argv or 'test_coverage' in sys.argv:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
