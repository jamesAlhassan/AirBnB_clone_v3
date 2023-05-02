#!/usr/bin/python3
'''Cities view module'''
from flask import jsonify, abort, request, make_response
from api.v1.views import app_views
from flasgger.utils import swag_from
from models import storage
from models.state import State
from models.city import City


@app_views.route('/states/<string:state_id>/cities',
                 methods=['GET'], strict_slashes=False)
@swag_from('resources/city/get.yml', methods=['GET'])
def getCity(state_id):
    """ Retrieves the list of all City objects of a State """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    list_cities = [obj.to_dict() for obj in state.cities]
    return jsonify(list_cities)


@app_views.route('/cities/<string:city_id>', methods=['GET'],
                 strict_slashes=False)
@swag_from('resources/city/getCityId.yml', methods=['GET'])
def getCityId(city_id):
    """ Get city by id"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    return jsonify(city.to_dict())


@app_views.route('/cities/<string:city_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('resources/city/deleteCity.yml', methods=['DELETE'])
def deleteCity(city_id):
    """ Delete city by id"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    city.delete()
    storage.save()
    return jsonify({})


@app_views.route('/states/<string:state_id>/cities', methods=['POST'],
                 strict_slashes=False)
@swag_from('resources/city/post.yml', methods=['POST'])
def createCity(state_id):
    """ Create City """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    if not request.get_json():
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    if 'name' not in request.get_json():
        return make_response(jsonify({"error": "Missing name"}), 400)

    js = request.get_json()
    ob = City(**js)
    ob.state_id = state.id
    ob.save()
    return jsonify(ob.to_dict()), 201


@app_views.route('/cities/<string:city_id>', methods=['PUT'],
                 strict_slashes=False)
@swag_from('resources/city/updateCity.yml', methods=['PUT'])
def Updatecity(city_id):
    """Update City  """
    if not request.get_json():
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    obj = storage.get(City, city_id)
    if obj is None:
        abort(404)
    for key, value in request.get_json().items():
        if key not in ['id', 'state_id', 'created_at', 'updated_at']:
            setattr(obj, key, value)
    storage.save()
    return jsonify(obj.to_dict())
