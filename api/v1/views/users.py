#!/usr/bin/python3
"""Users"""
from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.user import User


@app_views.route("/users", methods=['GET'], strict_slashes=False)
def get_users():
    """All users"""
    dic = []
    users = storage.all(User).items()
    for key, value in users:
        dic.append(value.to_dict())
    return jsonify(dic)


@app_views.route("/users/<user_id>", methods=['GET'], strict_slashes=False)
def by_id(user_id):
    """Get user by id"""
    user = storage.get(User, user_id)
    if user:
        return jsonify(user.to_dict())
    else:
        abort(404)


@app_views.route("/users/<user_id>", methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """Delete by id"""
    usr = storage.get(User, user_id)
    if usr:
        storage.delete(usr)
        storage.save()
        return jsonify({})
    else:
        abort(404)


@app_views.route('/users/', methods=['POST'], strict_slashes=False)
def create_user():
    """Post method"""
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'email' not in request.get_json():
        abort(400, description="Missing email")
    if 'password' not in request.get_json():
        abort(400, description="Missing password")
    kargs = request.get_json()
    user = User(**kargs)
    storage.new(user)
    storage.save()
    return (jsonify(user.to_dict()), 201)


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id):
    """Update method"""
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    json_dic = request.get_json()
    if not json_dic:
        abort(400, description="Not a JSON")
    for key, value in json_dict.items():
        if key not in ['id', 'created_at', 'updated_at', 'email']:
            setattr(user, key, value)
    storage.save()
    return (jsonify(user.to_dict()), 200)
