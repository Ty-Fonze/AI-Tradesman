from flask import Flask
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return "AI Backend is running!"

@socketio.on('message')
def handle_message(data):
    print('Received message:', data)
    emit('response', {'message': 'AI response here!'})

if __name__ == '__main__':
    socketio.run(app, debug=True)
