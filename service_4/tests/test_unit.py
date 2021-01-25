from unittest.mock import patch
from flask import url_for
from application import app
from flask_testing import TestCase

from os import getenv

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_common(self):
        test = {"location":"London", "weather":"Sunny"}

        response = self.client.post(url_for('get'), json=test_data)
        self.assertEqual('Avengers: Infinity War', response.data)

