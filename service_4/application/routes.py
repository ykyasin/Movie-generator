from application import app
from flask import request, Response, jsonify

@app.route('/movie', methods=["POST"])
def movie():
    in_uk = {"Clear" : "Avengers", "Rain" : "Paranormal", "Clouds" : "I am legend", "Other":"xyz"}
    out_uk = {"Clear" : "Avengers2", "Rain" : "Paranormal2", "Clouds" : "I am legend2", "Other":"xyz2"}
    
    info = request.json

    if info["country"] == "United Kingdom":
        if info["weather"] in in_uk:
            movie = in_uk[info["weather"]]
        else:
            movie = in_uk["Other"]
    else: 
        if info["weather"] in out_uk:
            movie = out_uk[info["weather"]]
        else:
            movie = out_uk["Other"]
    
    return Response(movie, mimetype='text/plain')