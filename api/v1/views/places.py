#!/usr/bin/pythone3
"""Places"""
from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.place import Place
from models.city import City
from models.user import User


@app_views.route('/cities/<city_id>/places', methods=['GET'], strict_slashes=False)
def places(city_id):
     """Get place in a specific city"""
     city = storage.get('City', city_id)
     if city is None:
         abort(404)
     places = []
     for place in city.places:
         places.append(place.to_dict())
     return jsonify(places)


@app_views.route('/places/<place_id>', methods=['GET'], strict_slashes=False)
def place_by_id(place_id):
    """Place by id """
    place = storage.get(Place, place_id)
    if place:
        return jsonify(place.to_dict())
    else:
        abort(404)


@app_views.route('/places/<place_id>', methods=['DELETE'], strict_slashes=False)
def delete_place(place_id):
    """Delete place"""
    place = storage.get(Place, place_id)
    if place:
        place.delete()
        storage.save()
        return jsonify({})
    else:
        abort (404)


@app_views.route('/cities/<city_id>/places', methods=['POST'], strict_slashes=False)
def create_place(city_id):
    """Create place"""
    city =storage.get(City, city_id)
    if not city:
        abort(404)
    req_json = request.get_json()
    if not req_json:
        abort(400, description="Not a JSON")
    if 'user_id' not in req_json:
        abort(400, description="Missing user_id")
    if 'name' not in req_json:
        abort(400, description="Missing name")
    req_json['city_id'] = city_id
    place = Place(**req_json)
    storage.new(place)
    storage.save()
    return (jsonify(place.to_dict()), 201)


@app_views.route('/places/<place_id>', methods=['PUT'], strict_slashes=False)
def update_place(place_id):
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    req_json = request.get_json()
    if not req_json:
        abort(400, description="Not a JSON")
    for key, value in req_json.items():
        if key not in ['id', 'created_at', 'updated_at', 'city_id', 'user_id']:
            setattr(place, key, value)
    storage.save()
    return (jsonify(place.to_dict()), 200)
