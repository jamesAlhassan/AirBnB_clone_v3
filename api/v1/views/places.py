#!/usr/bin/python3
'''
Place view module
'''
from flask import jsonify, abort, request, make_response
from api.v1.views import app_views
from models.place import Place
from flasgger.utils import swag_from
from models import storage
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.state import State
