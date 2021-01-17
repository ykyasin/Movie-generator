from application import app
from flask import request, Response
from random import choice

@app.route('/weather', methods=["GET"])
def weather():
    weather = ['Sunny','Rainy','Windy']
    return Response(choice(weather), mimetype='text/plain')