#!/usr/bin/python3
''' Route that returns JSON ok status'''
from api.v1.views import app_views
from flask import jsonify


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
