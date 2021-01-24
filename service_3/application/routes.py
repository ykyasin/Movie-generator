from application import app
from flask import request, Response, jsonify
from random import choice
import requests

@app.route('/weather', methods=["GET"])
def weather():
    weather = ['Sunny','Rainy','Windy']
    city = request.json
    api_key = "5a769573da91b09400e1d86ec1ca27bf"
    api_url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city, api_key)
    r = requests.get(api_url)
    weather_response = r.json()
    return jsonify(weather_response)

#http://api.openweathermap.org/data/2.5/weather?q=Tokyo&APPID=5a769573da91b09400e1d86ec1ca27bf
# x["weather"][0]["main"]
#api.openweathermap.org/data/2.5/weather?q=London&appid=5a769573da91b09400e1d86ec1ca27bf
#api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}