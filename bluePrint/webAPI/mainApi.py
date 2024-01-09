from flask import Blueprint, session, make_response
from flask import request, jsonify
import logging

main_api = Blueprint('main_api', __name__)


@main_api.route('/test')
def test():
    logger = logging.getLogger('base')
    logger.info('test')
    print(logger.__dict__)
    return ''


@main_api.route('/')
def index():
    """

    :return:
    """
    return 'this is api route'


@main_api.route('/cookie/get', methods=['GET'])
def get_cookie():
    resp = make_response('set cookies')
    resp.set_cookie('token', '123456')
    return resp


@main_api.route('/checkAlive')
def check_alive():
    """

    :return:
    """
    res = {
        'MESSAGE': 'app is alive',
        'STATUS': 'SUCCESS',
        'DATA': None
    }
    return jsonify(res)


@main_api.route('/requestRepeat', methods=['POST', 'GET'])
def request_repeat():
    """

    :return:
    """
    res = {
        'MESSAGE': None,
        'STATUS': None,
        'DATA': None
    }
    if request.method.upper() == 'POST':
        res['STATUS'] = 'SUCCESS'
        res['DATA'] = request.data
    elif request.method.upper() == 'GET':
        res['STATUS'] = 'SUCCESS'
        res['MESSAGE'] = 'hello'
    else:
        res['STATUS'] = 'FAILED'
    return jsonify(res)
