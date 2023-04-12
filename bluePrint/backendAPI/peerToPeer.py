"""
Author: li bo
date: 2023/3/23 14:13
"""
from flask import request, session, Blueprint

peer = Blueprint('peer', __name__)

room = [f'room_{x}' for x in range(12)]
@peer.route('/p2p/connect/<string:key>')
def connect_peer(key):
    pass

@peer.route('/p2p/alive_connect/<string:key>')
def alive_connect():
    pass
