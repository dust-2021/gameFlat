import hashlib

from flask import request, session, redirect, Blueprint
from sqlalchemy import or_
from db.mysqlDB import User, db_session
from etc.globalVar import AppGlobal
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
    hasher.update(password.encode('utf-8'))

    if AppGlobal.IS_THE_MASTER_MACHINE:
        user = User(username=username, passwordMD5=hasher.hexdigest())
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
    username = request.form.get('username')
    password = request.form.get('password')
    _pw = sha256(password.encode('utf-8'))


    true_user, true_pw = db_session.query(User.passwordMD5).filter_by().first()


@master.route('/new_machine', methods=['POST'])
def new_machine():
    pass
