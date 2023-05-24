from flask import request, session, redirect, Blueprint

master = Blueprint('master', __name__)

@master.route('/session_check')
def session_check():
    pass




