import unittest
from expects import *
from test.matchers.http import *

from app import app, db

class AppTestCase(unittest.TestCase):

    def setUp(self):
        app.config.from_object('config.application.TestingConfig')
        db.create_all()
        self.client = app.test_client(self)
    
    def test_index_it_returns_http_ok(self):
        response = self.client.get('/', content_type='text/html')
        assert response.status_code == 200

    def test_index_with_expect_it_returns_http_ok(self):
        response = self.client.get('/', content_type='text/html')
        expect(response).to(have_http_status_ok)


if __name__ == '__main__':
    unittest.main()
