from flask import Blueprint, request, jsonify
from app.realtime.websocket_manager import send_auth_request
realtime_bp = Blueprint('realtime', __name__)
@realtime_bp.route('/trigger-auth', methods=['POST'])
def trigger_auth():
    data = request.json
    user_id = data.get("user_id")
    send_auth_request(user_id, "Approve login?")
    return jsonify({"message": "Auth request sent"})
