#!/usr/bin/python3
"""routes of index module """
from api.v1.views import app_views
from flask import jsonify
from models import storage

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    ''' Returns "status": "OK" '''
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """ an endpoint that retrieves the number of each objects by type """
    classes = {"Amenity": "amenities", "City": "cities",
               "Place": "places", "Review": "reviews",
               "State": "states", "User": "users"}
    all_stats = {}
    for cls in classes.keys():
        all_stats[classes[cls]] = storage.count(cls)
    return jsonify(all_ stats)

