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
        response = self.client.post(url_for('movie'), json={"location":"London", "weather":"Sunny"})
        self.assertEqual(b"Avengers: Infinity War", response.data)

