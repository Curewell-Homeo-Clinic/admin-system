import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from decouple import config

from .settings import DEBUG

if DEBUG == False:
    print("Sentry is enabled")
    sentry_sdk.init(environment='PRODUCTION',
                    dsn=config('SENTRY_DSN'),
                    integrations=[DjangoIntegration()],
                    traces_sample_rate=1.0,
                    send_default_pii=True)