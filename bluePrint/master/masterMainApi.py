import hashlib
import re

from flask import request, session, redirect, Blueprint, url_for, jsonify
from sqlalchemy import or_
from db.mysqlDB import User, db_session
from etc.globalVar import AppConfig
from etc.tools.wrapper import set_period_request_count, session_checker
from hashlib import sha256
from apCelery.task import register_email_code, register_sms_code
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
    res = db_session.query(User.passwordMD5).filter_by(
        or_(User.phone_number == username, User.email_address == username)).first()
    if len(res) == 0:
        resp['STATUS'] = 500
        resp['MESSAGE'] = 'account already exist'
        return jsonify(resp)

    password = data.form.get('password')

    pw_hasher = hashlib.sha256()
    id_hasher = hashlib.sha256()
    pw_hasher.update((password + AppConfig.SECRET_KEY).encode('utf-8'))
    id_hasher.update((username + AppConfig.SECRET_KEY).encode('utf-8'))

    if re.match('\d{13}', username):
        resp['STATUS'] = 400
        resp['MESSAGE'] = 'haven\'t configure phone sms server'
    elif re.match('\w+@\w+\.com', username):
        resp['STATUS'] = 200
        resp['MESSAGE'] = 'SUCCESS'
        resp['DATA'] = {
            'task_id': register_email_code.delay(username)
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

    resp = {
        'STATUS': None,
        'MESSAGE': '',
        'DATA': None
    }
    if celery_redis.get(msg_code) == task_id:
        resp['STATUS'] = 200
        resp['MESSAGE'] = 'SUCCESS'
    else:
        resp['STATUS'] = 500
        resp['MESSAGE'] = 'FAILED'

    celery_redis.delete(task_id)
    return jsonify(resp)


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

    res = db_session.query(User.passwordMD5).filter_by(
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
    return redirect(url_for('page.index'))


@master.route('/modify_nickname', methods=['POST'])
@session_checker
def modify_nickname():
    """

    :return:
    """
    user_id = session.get('username')
    data = request.json


@master.route('/modify_password', methods=['POST'])
@session_checker
def modify_password():
    """

    :return:
    """
    user_id = session.get('username')
    data = request.json
    new_password = data.get('new_password')
    old_password = db_session.query(User.passwordMD5).filter_by(user_id=user_id).first()[0]
    hasher = hashlib.sha256()
    hasher.update((new_password + AppConfig.SECRET_KEY).encode('utf-8'))
    new_password_hash = hasher.hexdigest()

    if new_password_hash == old_password:
        res = {
            'STATUS': 0,
            'MESSAGE': 'new password is the same with the old password.',
            'DATA': None
        }
        return jsonify(res)


@master.route('/write_off_account', methods=['POST'])
@session_checker
def write_off_account():
    pass
