import os
import unittest

from tests.base import BaseTestCase

from app import app
from app import db

from app.models.post import Post


class TestHomeController(BaseTestCase):
    def test_home_it_returns_http_ok(self):
        response = self.client.get("/")
        self.assert200(response)
        self.assert_template_used("/application/home.html")


if __name__ == "__main__":
    unittest.main()
