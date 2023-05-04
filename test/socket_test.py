"""
Author: li bo
date: 2023/4/20 10:25
"""
import socketio

sio = socketio.Client()

@sio.event
def connect():
    print('connected to server')

@sio.event
def disconnect():
    print('disconnected from server')

@sio.on('my event')
def on_my_event(data):
    print('received data:', data)

if __name__ == '__main__':
    sio.connect('http://localhost:5000', wait_timeout=10)
    sio.emit('message', {'data': 'hello world'}, namespace='/socket')
    sio.wait()
