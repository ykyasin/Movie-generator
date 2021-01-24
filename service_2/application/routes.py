from application import app
from flask import request, Response, jsonify
import requests

def location():
    ip_address = request.environ['HTTP_X_FORWARDED_FOR']
    api_key = "80a3e9c5b548dfa6ca3d7cc727c1cc5e"
    
    api_url = "http://api.ipstack.com/{}?access_key={}".format(ip_address, api_key)

    response = requests.get(api_url)

    return response.json()["city"]

@app.route('/get', methods=["GET"])
def get():
    location = location()
    return jsonify({"location":location})