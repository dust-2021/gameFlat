from flask_socketio import SocketIO, disconnect, join_room, leave_room, rooms, close_room, emit
import logging
import socketio
from flask import request, session
from etc.globalVar import AppConfig, app_status
from db.redisConn import socket_redis

soc = SocketIO()


@soc.on('connect', namespace='/test')
def socket_test():
    ip = request.remote_addr
    port = request.url
    print(f'{ip}: {port} connected')


@soc.on('connect', namespace='/')
def socket_connect():
    if app_status.connected_user_count >= AppConfig.MAX_CONNECTION:
        emit('message', {'msg': 'mor'})
        disconnect()

    user_id = session.get('user_id')
    ip = request.headers.get('X-real-IP', request.remote_addr)
    if not user_id:
        disconnect()

    logger = logging.getLogger('user')
    logger.info(f'{user_id} connected from {ip}.')
    socket_redis.set(user_id, '')


@soc.on('disconnect', namespace='/')
def socket_disconnect():
    username = session.get('username')
    if username is None:
        return
    socket_redis.delete(username)


@soc.on('message', namespace='/')
def message(msg: str):
    return msg, 200


@soc.on('checkout_room', namespace='/')
def checkout_room():
    pass
