#!/usr/bin/python3
'''Cities view module'''
from flask import jsonify, abort, request, make_response
from api.v1.views import app_views
from flasgger.utils import swag_from
from models import storage
from models.state import State
from models.city import City


