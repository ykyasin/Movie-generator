from application import app
from flask import request, Response, jsonify
from random import choice

@app.route('/location', methods=["POST"])
def location():
    location = ['London','New York','Tokyo']
    ip_address = request.data.decode("utf-8")
    return Response(ip_address, mimetype='text/plain')