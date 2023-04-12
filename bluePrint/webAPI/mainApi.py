"""
Author: li bo
date: 2023/3/21 23:33
"""
import flask
from flask import Blueprint, url_for
from tools.doc.apiDoc import API_RETURN
from flask import request, session, jsonify
from db.mysqlDB import db_session
import logging

main_api = Blueprint('main_api', __name__)

@main_api.route('/test')
def test():
    logger = logging.getLogger('base')
    logger.info('test')
    return ''

@main_api.route('/')
def index():
    """

    :return:
    """
    return 'this is a flask website api route'


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
