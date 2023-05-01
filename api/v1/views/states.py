#!/usr/bin/python3
'''states view module'''
from flask import jsonify
from flasgger.utils import swag_from

@app_views.route('/states', methods=['GET'], strict_slashes=False)
@swag_from('documentation/state/get.yml', methods=['GET'])
def get_all_states():
    """ Get all states """
    all_states = [ob.to_dict() for ob in storage.all(State).values()]
    return jsonify(all_states)
