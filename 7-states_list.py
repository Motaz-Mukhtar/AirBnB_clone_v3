#!/usr/bin/python3
""" Start Flask Web Application """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.user import User


app = Flask(__name__)
app.url_map.strict_slashes=False


@app.route('/states_list')
def states_list():
    """ return list of State Objects """
    states = storage.all("User")
    print(states)
    return render_template('7-states_list.html', name=states)

@app.teardown_appcontext
def teardown(se):
    """ remove the currnet Session  """
    storage.close()

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port='5000', load_dotenv=True, debug=1)
