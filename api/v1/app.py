#!/usr/bin/python3
""" The main app """
from flask import Flask, jsonify, make_response
from models import storage
from api.v1.views import app_views
from os import environ

app = Flask(__name__)
app.register_blueprint(app_views, url_prefix="/api/v1")




@app.teardown_appcontext
def close_storage(x):
    """close storage"""
    storage.close()





if __name__ == "__main__":
    host = environ.get('HBNB_API_HOST')
    port = environ.get('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)
