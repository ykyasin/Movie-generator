from application import app
from flask import request, Response
from random import choice

@app.route('/location', methods=["GET"])
def location():
    location = ['London','New Delhi','Tokyo']
    return Response(choice(location), mimetype='text/plain') 