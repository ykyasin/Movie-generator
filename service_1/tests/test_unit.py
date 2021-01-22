from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app
import requests_mock

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_avengers(self):
        with requests_mock.mock() as m:
            m.get('http://movie-generator:5000/location', text='Tokyo')
            m.get('http://movie-generator:5000/weather', text='Sunny')
            m.post('http://movie-generator:5000/movie', text='Avengers')
            response = self.client.get(url_for('home'))
            self.assertIn(b'Movie today:' response.data)
