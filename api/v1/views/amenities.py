#!/usr/bin/python3
"""
    View for Amenity objects that handles all default
    RESTFul API actions:
"""
from api.v1.views import app_views
from models.amenity import Amenity
from flask import jsonify, abort, request
from models import storage


@app_views.route('/amenities', methods=['GET', 'POST'], strict_slashes=False)
def amenities():
    """
        in GET:
            Return all Amenities object
        in POST:
            Creates Amenity object, and Returns the new Amenity with
            the status code 201
            if the HTTP request body is not valid
            JSON raise 400 error with message Not a JSON.
            if the dictionary doesn't contain the key name
            raise 400 error with message Missing name
    """
    amenities = storage.all('Amenity')
    all_amenities = [amenity.to_dict() for key, amenity in amenities.items()]

    if request.method == 'GET':
        return jsonify(all_amenities)

    if request.method == 'POST':
        json_dict = request.get_json()

        if not request.json:
            abort(400, "Not a JSON")
        if 'name' not in json_dict:
            abort(400, "Missing name")

        amenity_instance = Amenity(**json_dict)
        storage.new(amenity_instance)
        storage.save()
        return jsonify(amenity_instance.to_dict()), 201


@app_views.route('/amenities/<amenity_id>', methods=['GET', 'DELETE', 'PUT'])
def amenity_by_id(amenity_id):
    """
        in GET:
            Return Amenity object by id, if the amneity_id is not linked
            to any Amenity object, raise a 404
        in DELETE:
            Deletes a Amenity object by id, and Returns an empty dictionary
            with status code 200.
            if the amenity_id is not linked to any Amenity object,
            raise a 404 error
        in PUT:
            Updates a Amenity object, and return it with the status code 200.
            Ignore keys: id, created_at and updated_at.
            return error 400 with the messave Not a JSON if the HTTP request
            body is not valid JSON.
    """
    all_amenities = storage.all('Amenity')
    amenity = storage.get('Amenity', amenity_id)

    if amenity is None:
        abort(404)

    if request.method == 'GET':
        return jsonify(amenity.to_dict())

    if request.method == 'DELETE':
        storage.delete(amenity)
        storage.save()
        return jsonify({}), 200

    if request.method == 'PUT':
        if not request.json:
            abort(400, "Not a JSON")

        amenity.name = request.get_json().get('name')
        storage.save()
        return jsonify(amenity.to_dict()), 200
