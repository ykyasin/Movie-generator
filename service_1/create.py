from application import db 
from application.models import User, Post
db.drop_all()
db.create_all()