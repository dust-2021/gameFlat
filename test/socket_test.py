import socketio

sio = socketio.Client()

@sio.event
def connect():
    print('connected')

@sio.event
def disconnected():
    print('disconnect')


if __name__ == '__main__':
    sio.connect('http://localhost:5000', wait_timeout=3)
    while True:
        sio.emit('message', {'data': 'hello world'})

