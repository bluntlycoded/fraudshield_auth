from flask import Blueprint, request, jsonify
from app.sessions.session_service import log_session
sessions_bp = Blueprint('sessions', __name__)
@sessions_bp.route('/log', methods=['POST'])
def log():
    data = request.json
    log_session(data.get("user_id"), data.get("device_id"), data.get("ip_address"))
    return jsonify({"message": "Session logged"})
