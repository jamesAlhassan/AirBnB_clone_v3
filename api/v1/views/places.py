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


@app_views.route('/places/<string:place_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('resources/places/deletePlace.yml', methods=['DELETE'])
def deletePlace(place_id):
    """ Delete place by id """
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    place.delete()
    storage.save()
    return jsonify({})


@app_views.route('/cities/<string:city_id>/places', methods=['POST'],
                 strict_slashes=False)
@swag_from('resources/places/post.yml', methods=['POST'])
def createPlace(city_id):
    """ Create new place """
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    if not request.get_json():
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    if 'user_id' not in request.get_json():
        return make_response(jsonify({"error": "Missing user_id"}), 400)
    if 'name' not in request.get_json():
        return make_response(jsonify({"error": "Missing name"}), 400)
    kwargs = request.get_json()
    kwargs['city_id'] = city_id
    user = storage.get(User, kwargs['user_id'])
    if user is None:
        abort(404)
    obj = Place(**kwargs)
    obj.save()


@app_views.route('/places/<string:place_id>', methods=['PUT'],
                 strict_slashes=False)
@swag_from('resources/places/updatePlace.yml', methods=['PUT'])
def post_place(place_id):
    """ Update by id """
    if not request.get_json():
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    obj = storage.get(Place, place_id)
    if obj is None:
        abort(404)
    for key, value in request.get_json().items():
        if key not in ['id', 'user_id', 'city_id', 'created_at', 'updated']:
            setattr(obj, key, value)
    storage.save()
    return jsonify(obj.to_dict())
    return (jsonify(obj.to_dict()), 201)


@app_views.route('/places_search', methods=['POST'],
                 strict_slashes=False)
@swag_from('resources/places/findPlace.yml', methods=['POST'])
def search_places_by_id():
    """ Find places by id """
    if request.get_json() is None:
        return make_response(jsonify({"error": "Not a JSON"}), 400)

    data = request.get_json()

    if data and len(data):
        states = data.get('states', None)
        cities = data.get('cities', None)
        amenities = data.get('amenities', None)

    if not data or not len(data) or (
            not states and
            not cities and
            not amenities):
        places = storage.all(Place).values()
        list_places = []
        for place in places:
            list_places.append(place.to_dict())
        return jsonify(list_places)

    list_places = []
    if states:
        states_obj = [storage.get(State, s_id) for s_id in states]
        for state in states_obj:
            if state:
                for city in state.cities:
                    if city:
                        for place in city.places:
                            list_places.append(place)

    if cities:
        city_obj = [storage.get(City, c_id) for c_id in cities]
        for city in city_obj:
            if city:
                for place in city.places:
                    if place not in list_places:
                        list_places.append(place)

    if amenities:
        if not list_places:
            list_places = storage.all(Place).values()
        amenities_obj = [storage.get(Amenity, a_id) for a_id in amenities]
        list_places = [place for place in list_places
                       if all([am in place.amenities
                               for am in amenities_obj])]

    places = []
    for p in list_places:
        d = p.to_dict()
        d.pop('amenities', None)
        places.append(d)

    return jsonify(places)
