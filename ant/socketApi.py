from flask_socketio import SocketIO, disconnect, join_room, leave_room, rooms, close_room, emit
import logging
import socketio
from flask import request, session
from etc.globalVar import AppConfig, AppStatus
from db.redisConn import socket_redis

soc = SocketIO()


@soc.on('connect')
def socket_connect():

    if AppStatus.CONNECTED_USER < AppConfig.MAX_CONNECTION:
        AppStatus.CONNECTED_USER += 1
    else:
        disconnect()
        return '', 200

    user_id = session.get('username')
    ip = request.headers.get('X-real-IP', request.remote_addr)
    data = request.json
    if not user_id:
        disconnect()
        return '', 200

    logger = logging.getLogger('user')
    logger.info(f'{user_id} connected from {ip}.')
    socket_redis.set(user_id, '')


@soc.on('disconnect')
def socket_disconnect():
    socket_redis.delete(session.get('username'))


@soc.on('message')
def message(data):
    soc.emit()


@soc.on('checkout_room')
def checkout_room():
    pass
