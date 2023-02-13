#!/usr/bin/python3
""" Start Flask Web Application """
from flask import Flask
from flask import render_template
from models import storage


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ return list of State Objects """
    states = storage.all("State")
    return render_template('7-states_list.html', name=states)


@app.teardown_appcontext
def teardown(se):
    """ remove the currnet Session  """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port="5000")
