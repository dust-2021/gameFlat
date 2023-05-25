from flask_socketio import SocketIO
import logging
from flask import request, session
from tools.wrapper import session_checker

soc = SocketIO()
@soc.on('connect')
@session_checker
def connect():
    user = session.get('user_id', request.headers.get('X-Real-IP', request.remote_addr))
    logger = logging.getLogger('user')
    logger.info(f'{user} connect to .')

    return 'success'


@soc.on('disconnect')
def disconnect():
    pass


@soc.on('message')
def message(data):
    print(data)

@soc.on('checkout_room')
def checkout_room():
    pass