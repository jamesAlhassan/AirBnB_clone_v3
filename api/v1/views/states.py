#!/usr/bin/python3
'''states view module'''
from flask import jsonify, abort
from api.v1.views import app_views
from flasgger.utils import swag_from
from models import storage
from models.state import State


@app_views.route('/states', methods=['GET'], strict_slashes=False)
@swag_from('resources/state/get.yml', methods=['GET'])
def get_all_states():
    """ Get all states """
    all_states = [ob.to_dict() for ob in storage.all(State).values()]
    return jsonify(all_states)


@app_views.route('/states/<string:state_id>', methods=['GET'],
                 strict_slashes=False)
@swag_from('resources/state/getId.yml', methods=['GET'])
def getStateId(state_id):
    """ Get state by id"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route('/states/<string:state_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('resources/state/delete.yml', methods=['DELETE'])
def deleteState(state_id):
    """ Delete state by id"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    state.delete()
    storage.save()
    return jsonify({})
