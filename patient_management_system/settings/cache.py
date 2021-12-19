from decouple import config

CACHE_TTL = 60 * 1500

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': config('REDIS_URL'),
        'OPTIONS': {
            'PASSWORD': config('REDIS_PASSWORD'),
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        },
        'KEY_PREFIX': 'curewell',
        'TIMEOUT': CACHE_TTL,
    }
}