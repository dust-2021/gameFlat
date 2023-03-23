"""
Author: li bo
date: 2023/3/21 23:33
"""
from flask import Blueprint
from tools.doc.apiDoc import API_RETURN
from flask import request, session, jsonify

mainApp = Blueprint('mainApp', __name__)


@mainApp.route('/checkAlive')
def check_alive():
    res = API_RETURN.copy()
    res['MESSAGE'] = 'app is alive'
    res['STATUS'] = 'SUCCESS'
    return jsonify(res)


@mainApp.route('/requestRepeat', methods=['POST', 'GET'])
def request_repeat():
    res = API_RETURN.copy()
    if request.method.upper() == 'POST':
        res['STATUS'] = 'SUCCESS'
        res['DATA'] = request.data
    elif request.method.upper() == 'GET':
        res['STATUS'] = 'SUCCESS'
        res['MESSAGE'] = 'hello'
    else:
        res['STATUS'] = 'FAILED'
    return jsonify(res)
