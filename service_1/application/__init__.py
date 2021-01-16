from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from os import getenv

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SECRET_KEY'] = "the pass"


from application import routes