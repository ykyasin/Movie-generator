from flask import Flask
from os import getenv

app = Flask(__name__)

def api_key():
    api_location = getenv("API_LOCATION") 
    return api_location

from application import routes