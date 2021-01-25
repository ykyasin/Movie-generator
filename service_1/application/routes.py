from application import app, db 
from flask import render_template
from sqlalchemy import desc
import requests

class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    weather = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(50), nullable=False)


@app.route('/')
@app.route('/home')
def home():
    location_response = requests.get('http://movie-gen_location_service:5000/location')
    weather_response = requests.get('http://movie-gen_weather_service:5000/weather')
    movie_response = requests.post("http://movie-gen_movie_service:5000/movie", json={"location":location_response.text, "weather":weather_response.text})

    new_movie = Movies(name=movie_response.text,weather=weather_response.text,location=location_response.text)
    db.session.add(new_movie)
    db.session.commit()

    previous_movies = Movies.query.order_by(desc('id')).limit(10).all() 

    return render_template('index.html', weather=weather_response.text, location=location_response.text, movie=movie_response.text, previous_movies=previous_movies)