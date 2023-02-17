#!/usr/bin/python3
""" Places reviews """
from models import storage
from api.v1.views import app_views
from flask import jsonify, abort, request
from models.review import Review
from models.user import User
from models.place import Place


@app_views.route("/places/<place_id>/reviews", methods=['GET'],
                 strict_slashes=False)
def review_by_id(place_id):
    """ Reviews by place id """
    review = []
    place = storage.all('Review')
    if place:
        for key, value in place.items():
            if value.to_dict()['place_id'] == place_id:
                review.append(value.to_dict())
        return jsonify(review)
    else:
        abort(404)


@app_views.route("/reviews/<review_id>", methods=['GET'],
                 strict_slashes=False)
def get_review(review_id):
    """ GET method"""
    review = storage.get(Review, review_id)
    if review:
        return jsonify(review.to_dict())
    else:
        abort(404)


@app_views.route("/reviews/<review_id>", methods=['DELETE'],
                 strict_slashes=False)
def delete_review(review_id):
    """ DELETE method"""
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    review.delete()
    storage.save()
    return (jsonify({}))


@app_views.route("/places/<place_id>/reviews", methods=['POST'],
                 strict_slashes=False)
def create_review(place_id):
    """ POST method """
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    kwargs = request.get_json()
    if "user_id" not in kwargs:
        abort(400, description="Missed user_id")
    user = storage.get(User, kwargs["user_id"])
    if user is None:
        abort(404)
    if "text" not in kwargs:
        abort(400, description="Missing text")
    kwargs['place_id'] = place_id
    review = Review(**kwargs)
    review.save()
    return (jsonify(review.to_dict()), 201)


@app_views.route("/reviews/<review_id>", methods=['PUT'], strict_slashes=False)
def put_review(review_id):
    """UPDATE review """
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    for key, val in request.get_json().items():
        if key not in ['id', 'user_id', 'place_id',
                       'created_at', 'updated_at']:
            setattr(review, key, val)
    storage.save()
    return (jsonify(review.to_dict()), 200)
