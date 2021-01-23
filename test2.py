import requests
from flask import Flask, request, Response, url_for

app = Flask(__name__)

@app.route("/test1", methods = ['GET','POST'])
def test1():
    city = "London"
    api_key1 = "80a3e9c5b548dfa6ca3d7cc727c1cc5e"
    api_key2 = "5a769573da91b09400e1d86ec1ca27bf"
    #api_url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city, api_key2)
    api_url = "http://api.ipstack.com/80.43.77.181?access_key={}".format(api_key1)
    r = requests.get(api_url)
    x = str(type(r))
    #return Response(r.json, status=200, mimetype="application/json")
    return r.json()

@app.route("/", methods = ['GET','POST'])
def test2():
    loc = requests.get("http://35.242.133.235:2000/test1")
    #"http://animal-noises_animal-backend:5000/animal")
    x = str(type(loc.json()))
    return loc.json()

app.run(host="0.0.0.0", port=2000)

#print(weather())
#api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}

#http://api.openweathermap.org/data/2.5/weather?q=Tokyo&APPID=5a769573da91b09400e1d86ec1ca27bf
# x["weather"][0]["main"]
#api.openweathermap.org/data/2.5/weather?q=London&appid=5a769573da91b09400e1d86ec1ca27bf
#api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}