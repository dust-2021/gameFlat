import hashlib
import re
import uuid

from flask import request, session, redirect, Blueprint, url_for, jsonify
from sqlalchemy import or_
from db.mysqlDB import User, db_session
from etc.globalVar import AppConfig
from etc.tools.wrapper import set_period_request_count, session_checker
from hashlib import sha256
from apCelery.task import register_email_code, register_sms_code
from celery.result import AsyncResult
from db.redisConn import celery_redis

master = Blueprint('master', __name__)


@master.route('/register', methods=['post'])
@set_period_request_count(5)
def register_user():
    """
    request json:
        {"username": string, "password": string}

    :return:
    """
    resp = {
        'STATUS': None,
        'MESSAGE': '',
        'DATA': None
    }
    data = request.json
    username = data.get('username')
    res = db_session.query(User.passwordMD5).filter(
        or_(User.phone_number == username, User.email_address == username)).first()
    if len(res) == 0:
        resp['STATUS'] = 500
        resp['MESSAGE'] = 'account already exist'
        return jsonify(resp)

    password = data.get('password')

    pw_hasher = hashlib.sha256()
    pw_hasher.update((password + AppConfig.SECRET_KEY).encode('utf-8'))

    if re.match('\d{13}', username):
        resp['STATUS'] = 400
        resp['MESSAGE'] = 'haven\'t configure phone sms server'
    elif re.match('\w+@\w+\.com', username):
        resp['STATUS'] = 200
        resp['MESSAGE'] = 'SUCCESS'
        resp['DATA'] = {
            'task_id': register_email_code.delay(username, username, pw_hasher.hexdigest())
        }
    else:
        resp['STATUS'] = 500
        resp['MESSAGE'] = 'unknown register type'
    return jsonify(resp)


@master.route('/register_code_check', methods=['POST'])
@set_period_request_count(5)
def register_code_check():
    """
    request json:
        {"task_id": string,"msg_code": string}
    :return:
    """
    data = request.json
    task_id = data.get('task_id')
    msg_code = data.get('msg_code')

    result = AsyncResult(task_id)
    resp = {
        'STATUS': None,
        'MESSAGE': '',
        'DATA': None
    }
    if not result.ready():
        resp['STATUS'] = 400
        resp['MESSAGE'] = 'code haven\'t yield yet.'
        return jsonify(resp)

    result = result.result
    if msg_code != result.get('code'):
        resp['STATUS'] = 500
        resp['MESSAGE'] = 'code different'

    user = User(user_id=uuid.UUID, )


@master.route('/login', methods=['POST'])
@set_period_request_count(5)
def login():
    """
    login route, the username must be a phone number or email number.
    request json:
        {"username": string, "password": string}
    :return:
    """
    data = request.json
    username = data.get('username')
    password = data.get('password') + AppConfig.SECRET_KEY
    _pw = sha256(password.encode('utf-8'))

    res = db_session.query(User.passwordMD5, User.user_id).filter(
        or_(User.phone_number == username, User.email_address == username)).first()
    resp = {
        'STATUS': None,
        'MESSAGE': '',
        'DATA': None
    }
    if len(res) == 0:
        resp['STATUS'] = 0
        resp['MESSAGE'] = ''
        return jsonify(resp)
    if _pw != res[0]:
        return
    session['user_id'] = res[1]
    session['username'] = username
    return redirect(url_for('page.index'))


@master.route('/modify_nickname', methods=['POST'])
@session_checker
def modify_nickname():
    """

    :return:
    """
    user_id = session.get('user_id')
    data = request.json


@master.route('/modify_password', methods=['POST'])
@session_checker
def modify_password():
    """

    :return:
    """
    user_id = session.get('user_id')
    data = request.json
    new_password = data.get('new_password')
    old_password = db_session.query(User.passwordMD5).filter_by(user_id=user_id).first()[0]
    hasher = hashlib.sha256()
    hasher.update((new_password + AppConfig.SECRET_KEY).encode('utf-8'))
    new_password_hash = hasher.hexdigest()

    if new_password_hash == old_password:
        res = {
            'STATUS': 500,
            'MESSAGE': 'new password is the same with the old password.',
            'DATA': None
        }
        return jsonify(res)


@master.route('/write_off_account', methods=['POST'])
@session_checker
def write_off_account():
    user_id = session.get('user_id')
