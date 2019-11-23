import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration


class SentryHelper():
    def __init__(self, app):
        self.app = app
        self.dsn = app.config.get("SENTRY_DSN")
        self.id = app.config.get("SENTRY_ID")
        self.env = app.config.get("ENV")
        self.__integrate()

    def __integrate(self):
        if (self.dsn and self.id) is None:
            return

        sentry_url = f"https://{ self.dsn }@sentry.io/{ self.id }"
        sentry_sdk.init(
            environment=self.env,
            dsn=sentry_url,
            integrations=[FlaskIntegration(), SqlalchemyIntegration()]
            )

