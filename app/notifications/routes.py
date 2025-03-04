from flask import Blueprint, request, jsonify
from app.notifications.notifications_service import send_notification
notifications_bp = Blueprint('notifications', __name__)
@notifications_bp.route('/send', methods=['POST'])
def notify():
    data = request.json
    send_notification(data.get("user_id"), data.get("message"))
    return jsonify({"message": "Notification sent"})
