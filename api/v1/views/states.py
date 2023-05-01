#!/usr/bin/python3
'''states view module'''
from flask import jsonify, abort
from flasgger.utils import swag_from


@app_views.route('/states', methods=['GET'], strict_slashes=False)
@swag_from('resources/state/get.yml', methods=['GET'])
def get_all_states():
    """ Get all states """
    all_states = [ob.to_dict() for ob in storage.all(State).values()]
    return jsonify(all_states)

@app_views.route('/states/<string:state_id>', methods=['GET'], strict_slashes=False)
@swag_from('resources/state/getIid.yml', methods=['GET'])
def getStateId(state_id):
    """ Get state by id"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict())
