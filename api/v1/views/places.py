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


@app_views.route('/cities/<string:city_id>/places',
                 methods=['GET'], strict_slashes=False)
@swag_from('resources/places/getPlace.yml', methods=['GET'])
def getPlace(city_id):
    """ Get places by id """
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    places = [obj.to_dict() for obj in city.places]
    return jsonify(places)


@app_views.route('/places/<string:place_id>', methods=['GET'],
                 strict_slashes=False)
@swag_from('resources/places/getPlaceId.yml', methods=['GET'])
def getPlaceId(place_id):
    """ Get place by id """
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    return jsonify(place.to_dict())
