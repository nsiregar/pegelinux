import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration


def init(app):
    sentry_dsn = app.config.get("SENTRY_DSN")
    sentry_id = app.config.get("SENTRY_ID")
    if (sentry_dsn and sentry_id) is None:
        return

    sentry_url = f"https://{ sentry_dsn }@sentry.io/{ sentry_id }"
    sentry_sdk.init(
        dsn=sentry_url,
        integrations=[FlaskIntegration()]
        )
