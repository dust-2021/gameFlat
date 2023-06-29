import hashlib
import re

from flask import request, session, redirect, Blueprint, url_for
from sqlalchemy import or_
from db.mysqlDB import User, db_session
from etc.globalVar import AppConfig
from etc.tools.wrapper import set_period_request_count
from hashlib import sha256

master = Blueprint('master', __name__)


@master.route('/register', methods=['post'])
@set_period_request_count(5)
def register_user():
    """

    :return:
    """
    username = request.form.get('username')
    password = request.form.get('password')

    hasher = hashlib.sha256()
    hasher.update((password + AppConfig.SECRET_KEY).encode('utf-8'))

    if re.match('\d{13}', username):
        user = User(phone_number=username, passwordMD5=hasher.hexdigest())
    elif re.match('\w+@\w+\.com', username):
        user = User(email_address=username, passwordMD5=hasher.hexdigest())
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
    :return:
    """
    user_id = request.form.get('username')
    password = request.form.get('password') + AppConfig.SECRET_KEY
    _pw = sha256(password.encode('utf-8'))

    res = db_session.query(User.passwordMD5).filter_by(user_id=user_id).first()
    if len(res) == 0:
        return
    if _pw != res[0]:
        return
    return redirect(url_for('page.index'))


@master.route('/new_machine', methods=['POST'])
def new_machine():
    pass
