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
from config.globalVar import AppGlobal

base_namespace = '/socket'

soc = SocketIO()


@soc.on('connect', namespace=base_namespace)
@session_checker
def connect(data):
    user = session.get('user_id', request.headers.get('X-Real-IP', request.remote_addr))
    logger = logging.getLogger('user')
    logger.info(f'{user} connect to .')

    room = data.get('', '')


@soc.on('disconnect', namespace=base_namespace)
def disconnect(data):
    pass


@soc.on('message', namespace=base_namespace)
def message(data):
    print(data)
