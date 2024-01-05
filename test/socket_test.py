import time

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
    sio.connect('http://localhost:5000', transports='websocket', namespaces=['/test'])
    while True:
        print('-')
        sio.emit('message', {'data': 'hello world'}, namespace='/test', callback=s_message)
        time.sleep(3)
