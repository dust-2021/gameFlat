"""
Author: li bo
date: 2023/4/19 16:16
"""
import flask
from flask_socketio import SocketIO
import logging
from flask import redirect, request, session
from tools.wrapper import session_checker
from typing import Union, List

base_namespace = '/socket'

GLOBAL_ROOM_LIST = []

soc = SocketIO()


@soc.on('connect', namespace=base_namespace)
def connect():
    user = session.get('user_id', request.headers.get('X-Real-IP', request.remote_addr))
    logger = logging.getLogger('user')
    logger.info(f'{user} connect to .')


@soc.on('disconnect', namespace=base_namespace)
def disconnect():
    pass


@soc.on('message', namespace=base_namespace)
def message(msg):
    print(msg)
