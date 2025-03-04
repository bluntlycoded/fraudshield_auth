from flask_socketio import SocketIO
socketio = SocketIO(message_queue='redis://')
connections = {}
def connect_websocket(user_id, sid):
    connections[user_id] = sid
def send_auth_request(user_id, message):
    if user_id in connections:
        socketio.emit('auth_request', {'message': message}, room=connections[user_id])
