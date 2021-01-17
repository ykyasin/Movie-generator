from application import app
from flask import request, Response

@app.route('/movie', methods=["POST"])
def movie():
    movies = {"Sunny" : "Avengers", "Rainy" : "Paranormal", "Windy" : "I am legend"}
    weather = request.data.decode("utf-8")
    return Response(movies[weather], mimetype='text/plain')