from flask import Flask
from app.database import firebase_config
from app.auth.routes import auth_bp
from app.users.routes import users_bp
from app.devices.routes import devices_bp
from app.sessions.routes import sessions_bp
from app.notifications.routes import notifications_bp
from app.realtime.websocket_routes import realtime_bp
def create_app():
    app = Flask(__name__)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(users_bp, url_prefix='/users')
    app.register_blueprint(devices_bp, url_prefix='/devices')
    app.register_blueprint(sessions_bp, url_prefix='/sessions')
    app.register_blueprint(notifications_bp, url_prefix='/notifications')
    app.register_blueprint(realtime_bp, url_prefix='/realtime')
    return app
