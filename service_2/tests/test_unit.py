from unittest.mock import patch
from flask import url_for
from application import app
from flask_testing import TestCase

from os import getenv

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_movie(self):
        with patch("choice") as random:
            random.return_value = "London" 
            response = self.client.get(url_for('location'))
            self.assertEqual(b'London', response.data)

        for x in range(50):
            response = self.client.get(url_for('location'))
            self.assertIn(response.data, [b"London", b"New Delhi", b"Tokyo"])
