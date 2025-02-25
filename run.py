from app import create_app
from flask_socketio import SocketIO
from flask import render_template

app = create_app()

@app.route("/")
def index():
    return render_template("index.html")

socketio = SocketIO(app)
if __name__ == "__main__":
    socketio.run(app,allow_unsafe_werkzeug=True)
