#!/usr/bin/python3
"""
    Create a new view for City objects that
    handles all default RESTFul API actions
"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.city import City


@app_views.route('states/<state_id>/cities', methods=['GET', 'POST'],
                 strict_slashes=False)
def cities(state_id):
    """
        in GET:
            Return list of all City objects linked to State by id
        in POST:
            Creates a City object
    """
    states = storage.all('State')
    state = storage.get('State', state_id)
    all_cities = []

    if state is None:
        abort(404)

    if request.method == 'GET':
        all_cities = [city.to_dict() for city in state.cities]
        return jsonify(all_cities)

    if request.method == 'POST':
        json_dict = request.get_json()

        if not request.json:
            abort(400, "Not a JSON")
        if 'name' not in json_dict:
            abort(400, "Missing name")
        city_instance = City(**json_dict)
        city_instance.state_id = state_id
        storage.new(city_instance)
        storage.save()
        return jsonify(city_instance.to_dict()), 201


@app_views.route('/cities/<city_id>', methods=['GET', 'DELETE', 'PUT'],
                 strict_slashes=False)
def city_by_id(city_id):
    """
        in GET:
            Return City object by id
        in DELETE:
            Deletes a City object
    """
    city = storage.get('City', city_id)
    cities = storage.all('City')

    if city is None:
        abort(404)

    if request.method == 'GET':
        return jsonify(city.to_dict())

    if request.method == 'DELETE':
        storage.delete(city)
        storage.save()
        return jsonify({}), 200

    if request.method == 'PUT':
        json_dict = request.get_json()

        if not request.json:
            abort(400, "Not a JSON")

        city.name = json_dict.get('name')
        storage.save()
        return jsonify(city.to_dict()), 200
