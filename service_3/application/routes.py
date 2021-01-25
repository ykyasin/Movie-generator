from application import app
from flask import request, Response, jsonify
from random import choice
import requests

@app.route('/weather', methods=["POST"])
def weather():
    city = request.json
    lat = city["latitude"]
    lon = city["longitude"]
    api_key = "5a769573da91b09400e1d86ec1ca27bf"
    #api_key = api_key()
    api_url = "http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}".format(lat,lon, api_key)
    
    response = requests.get(api_url)
    response = response.json()
    return jsonify(response)
