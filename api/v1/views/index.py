#!/usr/bin/python3
''' Route that returns JSON ok status'''
from api.v1.views import app_views
from flask import Flask, jsonify


@app_views.route('/status', strict_slashes=False)
def okStatus():
    """
    Returns a JSON ok status
    """
    return jsonify({"status": "OK"})
