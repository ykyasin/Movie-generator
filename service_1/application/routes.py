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
    ip_address = request.environ['HTTP_X_FORWARDED_FOR']
    
    location_response = requests.post('http://movie-gen_location_service:5000/location', data=ip_address) 
    weather_response = requests.post('http://movie-gen_location_service:5000/location', json=location_response.json())
    movie_response = "Avengers"

    lat = location_response["latitude"]
    lon = location_response["longitude"]
    #city = "London"
    api_key = "5a769573da91b09400e1d86ec1ca27bf"
    api_url = "http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}".format(lat, lon, api_key)
    response = requests.get(api_url)
    movie_response = response
    #new_movie = Movies(name=movie_response.text,weather=weather_response.text,location=location_response.text)
    #db.session.add(new_movie)
    #db.session.commit() 

    return render_template('index.html', location=location_response.json()["city"], weather=weather_response.text, movie=movie_response)