from application import app

@app.route('/')
@app.route('/home')
def home():
    return "It works"