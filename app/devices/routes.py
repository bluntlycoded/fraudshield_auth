from flask import Blueprint, request, jsonify
from app.devices.device_service import register_device, mark_device_as_trusted
devices_bp = Blueprint('devices', __name__)
@devices_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    register_device(data.get("user_id"), data.get("device_id"), data.get("device_name"))
    return jsonify({"message": "Device registered"})
@devices_bp.route('/trust', methods=['POST'])
def trust():
    data = request.json
    mark_device_as_trusted(data.get("device_id"))
    return jsonify({"message": "Device marked as trusted"})
