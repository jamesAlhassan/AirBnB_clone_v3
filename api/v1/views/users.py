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


@app_views.route('/users/<string:user_id>', methods=['GET'],
                 strict_slashes=False)
@swag_from('resources/user/getUserId.yml', methods=['GET'])
def getUser(user_id):
    """ Get user by id"""
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_dict())


@app_views.route('/users/<string:user_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('resources/user/deleteUser.yml', methods=['DELETE'])
def deleteUser(user_id):
    """ Delete user by id"""
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    user.delete()
    storage.save()
    return jsonify({})
