import hashlib

from flask import request, session, redirect, Blueprint

from db.mysqlDB import User, db_session
from etc.globalVar import AppGlobal

master = Blueprint('master', __name__)


@master.route('/register', methods=['post'])
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
def login():
    if AppGlobal.IS_THE_MASTER_MACHINE:
        pass

@master.route('/new_machine', methods=['POST'])
def new_machine():
    pass


