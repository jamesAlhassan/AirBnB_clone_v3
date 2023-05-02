#!/usr/bin/python3
'''
Amenity view Module
'''
from flask import jsonify, abort, request, make_response
from flasgger.utils import swag_from
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity


@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
@swag_from('resources/amenity/get.yml', methods=['GET'])
def getAmenities():
    """ Get amenities by id """
    all_list = [obj.to_dict() for obj in storage.all(Amenity).values()]
    return jsonify(all_list)


@app_views.route('/amenities/<string:amenity_id>', methods=['GET'],
                 strict_slashes=False)
@swag_from('resources/amenity/getAmenityId.yml', methods=['GET'])
def getAmenity(amenity_id):
    """ Get amenity by id"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    return jsonify(amenity.to_dict())


@app_views.route('/amenities/<string:amenity_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('resources/amenity/deleteAmenity.yml', methods=['DELETE'])
def deleteAmenity(amenity_id):
    """ Deletes amenity by id"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    amenity.delete()
    storage.save()
    return jsonify({})
