from application import app
from flask import request, Response, jsonify
from random import choice

@app.route('/location', methods=["GET"])
def location():
    location = ['London','New York','Tokyo']
    return Response(choice(location), mimetype='text/plain')