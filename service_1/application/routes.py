from application import app, db, api_key
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
    if 'HTTP_X_FORWARDED_FOR' in request.environ:
        ip_address = request.environ['HTTP_X_FORWARDED_FOR']
    else:
        ip_address = request.remote_addr
    api_location = api_key("location")
    api_weather = api_key("weather")
    #location_response = requests.post('http://movie-gen_location_service:5000/location', data=ip_address) 
    #location_response = requests.post('http://movie-gen_location_service:5000/location', json={"ip_address":ip_address, "api_key":api_location}) 
    #weather_response = requests.post('http://movie-gen_weather_service:5000/weather', json=location_response.json())
    
    #location = location_response.json()["city"]
    location = "London"
    #country = location_response.json()["country_name"]
    county = "United Kingdom"
    #weather = weather_response.json()["weather"][0]["main"]
    weather = "Rain"
    json_dict = {"country":country, "weather":weather}
    movie_response = requests.post('http://movie-gen_movie_service:5000/movie', json=json_dict)

    #new_movie_history = Movies(name=movie_response.text,weather=weather,location=location)
    #db.session.add(new_movie_history)
    #db.session.commit() 

    return render_template('index.html', location=location, weather=weather, movie=movie_response.text, ip_address =api_location)