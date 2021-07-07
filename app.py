from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    """ Returns simple welcome greeting. """

    return "<html><body><h1>welcome</h1></body></html>"

@app.route('/welcome/<location>')
def welcome_location(location):
    """ Returns welcome greeting to specific location. """
    
    return f"<html><body><h1>welcome {location}</h1></body></html>"
