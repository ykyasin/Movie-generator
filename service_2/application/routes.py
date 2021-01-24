from application import app
from flask import request, Response, jsonify

@app.route('/location', methods=["POST"])
def location():
    ip_address = request.data.decode("utf-8")
    api_key = "80a3e9c5b548dfa6ca3d7cc727c1cc5e"
    api_url = "http://api.ipstack.com/{}?access_key={}".format(ip_address, api_key)
    r = requests.get(api_url)
    json_object = response.json()
    return Response(json_object["city"], mimetype='text/plain')