#!/usr/bin/python3
'''
Amenity view Module
'''
from flask import jsonify, abort, request, make_response
from flasgger.utils import swag_from
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
