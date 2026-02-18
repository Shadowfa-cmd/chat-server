import eventlet
eventlet.monkey_patch()

import os
from flask import Flask
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/")
def home():
    return "Chat Server is Running!"

@socketio.on("message")
def handle_message(msg):
    send(msg, broadcast=True)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    socketio.run(app, host="0.0.0.0", port=port)