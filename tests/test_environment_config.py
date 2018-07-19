import unittest
from flask_testing import TestCase
from app import app


class TestEnvironmentConfig(TestCase):
    def create_app(self):
        app.config.from_object("config.application.TestingConfig")
        return app

    def test_environment_is_testing(self):
        self.assertTrue(app.config.get("TESTING") == True)
        self.assertFalse(app.config.get("SQLALCHEMY_TRACK_MODIFICATIONS"))
