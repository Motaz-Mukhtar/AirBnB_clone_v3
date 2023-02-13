#!/usr/bin/python3
""" Starts a Flask web application: """
from flask import Flask, render_template


app = Flask(__name__)
app.url_map_strict_slashes = False


@app.route('/')
def root():
    """ return Hello "HBNB!" at / """
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """ return "HBNB" at /hbnb """
    return "HBNB"


@app.route('/c/<text>')
def text(text):
    """ Dispaly text variable and replace '_' with ' ' """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def default_text(text):
    """ Dispaly text variable and replcae '_' with space ' '
        and 'is cool' by default
    """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number(n):
    """ Dispaly n only if an integer """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """ Display a HTML page only if n is an integer """
    return render_template('5-number.html', name=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    return render_template('6-number_odd_or_even.html', name=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
