import hashlib
from flask import Blueprint
from tools.doc.apiDoc import API_RETURN
from flask import request, jsonify
from db.mysqlDB import db_session
import logging
from db.mysqlDB import User
from etc.globalVar import AppGlobal

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


@main_api.route('/checkAlive')
def check_alive():
    """

    :return:
    """
    res = API_RETURN.copy()
    res['MESSAGE'] = 'app is alive'
    res['STATUS'] = 'SUCCESS'
    return jsonify(res)


@main_api.route('/requestRepeat', methods=['POST', 'GET'])
def request_repeat():
    """

    :return:
    """
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

