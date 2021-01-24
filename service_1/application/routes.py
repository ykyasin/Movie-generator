from application import app, db 
from flask import render_template, jsonify, request
import requests
import json

class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    weather = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(50), nullable=False)


@app.route('/')
@app.route('/home')
def home():
    #ip_address = request.environ['HTTP_X_FORWARDED_FOR']
    
    location_response = requests.get('http://movie-gen_location_service:5000/location') 
    #location = location_response.json()

    weather_response = "some"
    movie_response = "Avengers"

    #new_movie = Movies(name=movie_response.text,weather=weather_response.text,location=location_response.text)
    #db.session.add(new_movie)
    #db.session.commit() 

    return render_template('index.html', location=location_response.json()["city"], weather=weather_response, movie=movie_response)