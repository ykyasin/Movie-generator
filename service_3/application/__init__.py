from flask import Flask
from os import getenv

app = Flask(__name__)

def api_key():
    api_weather = getenv("API_WEATHER") 
    return api_weather

from application import routes