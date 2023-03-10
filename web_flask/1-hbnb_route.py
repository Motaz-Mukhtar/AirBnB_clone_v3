#!/usr/bin/python3
""" Starts a Flask web application: """
from flask import Flask


app = Flask(__name__)
app.url_map_strict_slashes = False


@app.route('/')
def root():
    """ return Hello "HBNB!" at / """
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """ return "HBNB" at /hbnb  """
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
