import socketio

sio = socketio.Client()

if __name__ == '__main__':
    sio.connect('http://localhost:5000', wait_timeout=3)
    # sio.emit('message', {'data': 'hello world'}, namespace='/socket')
    sio.wait()
