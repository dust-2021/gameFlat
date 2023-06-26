from flask_socketio import SocketIO, disconnect, join_room, leave_room
import logging
from flask import request, session
from etc.globalVar import AppConfig
from db.redisConn import socket_redis

soc = SocketIO()
@soc.on('connect')
def connect():
    username = session.get('username')
    ip = request.headers.get('X-real-IP', request.remote_addr)
    if not username:
        disconnect()

    logger = logging.getLogger('user')
    logger.info(f'{username} connected at {ip}.')
    socket_redis.set(username, '')



@soc.on('disconnect')
def disconnect():
    socket_redis.delete(session.get('username'))


@soc.on('message')
def message(data):
    print(data)

@soc.on('checkout_room')
def checkout_room():
    pass