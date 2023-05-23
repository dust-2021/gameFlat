import hashlib
import requests
import flask
from flask import Blueprint, url_for
from tools.doc.apiDoc import API_RETURN
from flask import request, session, jsonify
from db.mysqlDB import db_session
import logging
from db.mysqlDB import User
from config.globalVar import AppGlobal

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


@main_api.route('/register', methods=['post'])
def register_user():
    """

    :return:
    """
    username = request.form.get('username')
    password = request.form.get('password')

    hasher = hashlib.sha256()
    hasher.update(password.encode('utf-8'))

    if AppGlobal.IS_THE_MASTER_MACHINE:
        user = User(username=username, passwordMD5=hasher.hexdigest())
        db_session.add(user)
        db_session.commit()
        db_session.close()


@main_api.route('/login', methods=['POST'])
def login():
    if AppGlobal.IS_THE_MASTER_MACHINE:
        pass
