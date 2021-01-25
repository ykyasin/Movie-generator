from application import app
from flask import request, Response, jsonify
import requests 

@app.route('/location', methods=["POST"])
def location():
    info = request.json
    ip_address = info["ip_address"]
    api_key = info["api_key"]
    #api_key = "80a3e9c5b548dfa6ca3d7cc727c1cc5e"
    #api_key = api_key()
    api_url = "http://api.ipstack.com/{}?access_key={}".format(str(ip_address), api_key)
    
    response = requests.get(api_url)
    return jsonify(response.json())
