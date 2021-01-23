import requests
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def weather():
    y = request.remote_addr
    city = "London"
    api_key1 = "80a3e9c5b548dfa6ca3d7cc727c1cc5e"
    api_key2 = "5a769573da91b09400e1d86ec1ca27bf"
    api_url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city, api_key2)
    r = requests.get(api_url)
    x = r.json()["weather"][0]["main"]
    return x + y

app.run(host="0.0.0.0", port=2000)
#print(weather())
#api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}

#http://api.openweathermap.org/data/2.5/weather?q=Tokyo&APPID=5a769573da91b09400e1d86ec1ca27bf
# x["weather"][0]["main"]
#api.openweathermap.org/data/2.5/weather?q=London&appid=5a769573da91b09400e1d86ec1ca27bf
#api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}