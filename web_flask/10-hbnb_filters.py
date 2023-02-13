#!/usr/bin/python3
""" Start Flask Web Application, listen in 0.0.0.0 port 5000"""
from flask import Flask
from flask import render_template
from models import storage


app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """ Load State, City and Amentiy objects from DBStorage """
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html", states=states,
                           amenities=amenities)


@app.teardown_appcontext
def teardown(se):
    """ remove the currnet Session  """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port="5000", debug=1)
