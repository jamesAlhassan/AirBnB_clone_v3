#!/usr/bin/python3
''' Route that returns JSON ok status'''
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', strict_slashes=False)
def okStatus():
    """
    Returns a JSON ok status
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def noOfObject():
    """
    Retrieves the number of each objects by type
    """
    return jsonify({"amenities": storage.count("Amenity"),
                    "cities": storage.count("City"),
                    "places": storage.count("Place"),
                    "reviews": storage.count("Review"),
                    "states": storage.count("State"),
                    "users": storage.count("User")})
