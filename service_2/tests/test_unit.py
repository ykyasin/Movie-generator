from unittest.mock import patch
from flask import url_for
from application import app
from flask_testing import TestCase

from os import getenv

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_location(self):
        with patch("random.choice") as random:
            random.return_value = "Tokyo"
            response = self.client.get(url_for('location'))
            self.assertEqual(b'Tokyo', response.data)
