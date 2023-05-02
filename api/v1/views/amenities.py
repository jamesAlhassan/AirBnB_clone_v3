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
