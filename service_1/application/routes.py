from application import app
from flask import render_template
import requests

@app.route('/')
@app.route('/home')
def home():
    location_response = requests.get('http://location_service:5000/location')
    weather_response = requests.get('http://weather_service:5000/weather')
    movie_response = requests.post("http://movie_service:5000/movie", data=weather_response.text)

    return render_template('index.html', weather=weather_response.text, location=location_response.text, movie=movie_response.text)