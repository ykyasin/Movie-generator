from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)

def api_key(api):
    if api = "location"
        return getenv("API_LOCATION") 
    elif api = "weather"
        return getenv("API_WEATHER")
    return "Invalid key"

from application import routes