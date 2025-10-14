from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO, emit

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/")
def index():
    return "VisionLink Backend"

# SocketIO Signaling
@socketio.on("offer")
def handle_offer(data):
    emit("offer", data, broadcast=True, include_self=False)

@socketio.on("answer")
def handle_answer(data):
    emit("answer", data, broadcast=True, include_self=False)

@socketio.on("ice-candidate")
def handle_ice(data):
    emit("ice-candidate", data, broadcast=True, include_self=False)

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=5000)
