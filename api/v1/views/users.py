#!/usr/bin/python3
'''
Users view Module
'''
from flask import jsonify, abort, request, make_response
from api.v1.views import app_views
from flasgger.utils import swag_from
from models import storage
from models.user import User


@app_views.route('/users', methods=['GET'], strict_slashes=False)
@swag_from('resources/user/get.yml', methods=['GET'])
def getUsers():
    """ Get users"""
    all_users = [obj.to_dict() for obj in storage.all(User).values()]
    return jsonify(all_list)
