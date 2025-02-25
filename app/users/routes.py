from flask import Blueprint, jsonify
from app.users.user_service import get_user
users_bp = Blueprint('users', __name__)
@users_bp.route('/<user_id>', methods=['GET'])
def read_user(user_id):
    return jsonify(get_user(user_id))
