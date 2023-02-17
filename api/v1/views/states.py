#!/usr/bin/python3
"""
    View for State objects that handles all default
    RESTFul API actions:
"""
from api.v1.views import app_views
from flask import jsonify, abort, make_response, request
from models import storage
from models.state import State


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def states():
    """ Return All State objects """
    all_states = []

    for key, value in storage.all('State').items():
        all_states.append(value.to_dict())

    return jsonify(all_states)


@app_views.route('/states/<state_id>', methods=['GET'],
                 strict_slashes=False)
def state(state_id):
    """ Return State object by id """

    state = storage.get('State', state_id)

    if state is None:
        abort(404)

    return jsonify(state.to_dict())


@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def state_delete(state_id):
    """ Deletes a State object """
    key = 'State.{}'.format(state_id)
    all_states = storage.all('State')

    if key not in all_states:
        abort(404)

    storage.delete(all_states[key])
    storage.save()
    return jsonify({}), 200


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def state_post():
    """ Creates a State object """
    if not request.json:
        abort(400, 'Not a JSON')

    json_dict = request.get_json()

    if 'name' not in json_dict:
        abort(400, 'Missing name')

    new_state = State(**json_dict)
    storage.new(new_state)
    storage.save()
    return jsonify(new_state.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def state_put(state_id):
    """ Updates a State object """
    state_obj = storage.get('State', state_id)
    json_dict = request.get_json()

    if state_obj is None:
        abort(404)

    if not request.json:
        return abort(400, 'Not a JSON')

    state_obj.name = json_dict.get('name')
    storage.save()
    return jsonify(state_obj.to_dict()), 200
