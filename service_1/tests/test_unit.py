from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app, db
from os import getenv
import requests_mock

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI=getenv("TEST_DATABASE_URI"),
            WTF_CSRF_ENABLED=False,
            DEBUG=True
        )
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestResponse(TestBase):

    def test_avengers(self):
        with requests_mock.mock() as m:
            m.get('http://movie-generator:5000/location', text='Tokyo')
            m.get('http://movie-generator:5000/weather', text='Sunny')
            m.post('http://movie-generator:5000/movie', text='Avengers')
            response = self.client.get(url_for('home'))
            self.assertIn("Avengers")
