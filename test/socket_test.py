"""
Author: li bo
date: 2023/4/20 10:25
"""
import time

import socketio
import socket
import websockets


def sol():
    ws = websockets.WebSocketServer()
    bind = '127.0.0.1'
    port = 5000
    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    soc.connect((bind, port))

    while True:
        soc.send('connect'.encode('utf-8'))
        time.sleep(5)


if __name__ == '__main__':
    sol()
