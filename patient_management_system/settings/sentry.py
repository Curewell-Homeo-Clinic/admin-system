import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from decouple import config

sentry_sdk.init(dsn=config('SENTRY_DSN'),
                integrations=[DjangoIntegration()],
                traces_sample_rate=1.0,
                send_default_pii=True)