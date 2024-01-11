import time

import requests
import socketio

sio = socketio.Client()


@sio.on('connect')
def s_connect():
    print('connected')


@sio.on('disconnect')
def s_disconnected():
    print('disconnect')


@sio.on('message')
def s_message(msg):
    print(f'received : {msg}')


if __name__ == '__main__':
    headers = {

    }
    # resp = requests.post('127.0.0.1:500/master/login')
    sio.connect('http://localhost:5000', transports='websocket', namespaces=['/test', '/'])
    while True:
        print('-')
        sio.emit('message', {'data': 'hello world'}, callback=s_message)
        time.sleep(3)
