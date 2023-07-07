import hashlib
import re

from flask import request, session, redirect, Blueprint, url_for
from sqlalchemy import or_
from db.mysqlDB import User, db_session
from etc.globalVar import AppConfig
from etc.tools.wrapper import set_period_request_count, session_checker
from hashlib import sha256

master = Blueprint('master', __name__)


@master.route('/register', methods=['post'])
@set_period_request_count(5)
def register_user():
    """
    request json:
        {'username': '', 'password': ''}

    :return:
    """
    data = request.json
    username = data.get('username')
    password = data.form.get('password')

    pw_hasher = hashlib.sha256()
    id_hasher = hashlib.sha256()
    pw_hasher.update((password + AppConfig.SECRET_KEY).encode('utf-8'))
    id_hasher.update((username + AppConfig.SECRET_KEY).encode('utf-8'))

    if re.match('\d{13}', username):
        user = User(user_id=id_hasher.hexdigest(), phone_number=username, passwordMD5=pw_hasher.hexdigest())
    elif re.match('\w+@\w+\.com', username):
        user = User(user_id=id_hasher.hexdigest(), email_address=username, passwordMD5=pw_hasher.hexdigest())
    else:
        return
    db_session.add(user)
    db_session.commit()
    db_session.close()


@master.route('/login', methods=['POST'])
@set_period_request_count(5)
def login():
    """
    login route, the username must be a phone number or email number.
    request json:
        {'username': '', 'password': ''}
    response json:
        None
        redirect to wrong page or index page.
    :return:
    """
    data = request.json
    user_id = data.get('username')
    password = data.get('password') + AppConfig.SECRET_KEY
    _pw = sha256(password.encode('utf-8'))

    res = db_session.query(User.passwordMD5).filter_by(
        or_(User.phone_number == user_id, User.email_address == user_id)).first()
    if len(res) == 0:
        return
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

