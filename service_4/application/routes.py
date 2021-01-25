from application import app
from flask import request, Response

@app.route('/movie', methods=["POST"])
def movie():
    movies = {
    "London" : {"Sunny" : "Avengers: Infinity War", "Rainy" : "Schindler's List", "Windy" : "The Shawshank Redemption"},
    "New Delhi" : {"Sunny" : "Khaali Peeli", "Rainy" : "Bulbbul", "Windy" : "Devdas"},
    "Tokyo" : {"Sunny" : "Rurouni Kenshin", "Rainy" : "Ring", "Windy" : "Midnight Sun "}
    }
    info = request.json
    return Response(movies[info["location"]][info["weather"]], mimetype='text/plain')