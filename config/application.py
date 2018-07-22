import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "itsasecret"
    MAX_DEPTH = 5
    MAILGUN_API_KEY = os.environ.get("MAILGUN_API_KEY")
    MAILGUN_USER = os.environ.get("MAILGUN_USER")
    MAILGUN_DOMAIN = os.environ.get("MAILGUN_DOMAIN")
    MAILGUN_URL = "https://api.mailgun.net/v3/{}/messages".format(MAILGUN_DOMAIN)
    GITHUB_CLIENT_ID = os.environ.get("GITHUB_CLIENT_ID")
    GITHUB_SECRET_ID = os.environ.get("GITHUB_SECRET_ID")


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SECRET_KEY = os.environ.get("SECRET_KEY") or "development_key"
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(BASE_DIR.strip("\\config"), "db/dev.db")
    # SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@127.0.0.1:5432/pegelblogs"


class TestingConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "db/test.db")


class ProductionConfig(BaseConfig):
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
