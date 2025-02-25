from flask import Blueprint, request, jsonify, send_file
from app.auth.auth_service import create_user, send_password_reset
from app.auth.otp_service import generate_otp, verify_otp
from app.auth.totp_service import generate_qr_code, verify_totp_code
from app.auth.webauthn_service import register_webauthn
import jwt
from firebase_admin import auth as firebase_auth
from app.config.config import SECRET_KEY

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    try:
        user = create_user(email, password)
        return jsonify({"message": "User created", "user": user})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    try:
        user = firebase_auth.get_user_by_email(email)
        token = jwt.encode({"uid": user.uid}, SECRET_KEY, algorithm="HS256")
        return jsonify({"token": token})
    except Exception:
        return jsonify({"error": "Invalid credentials"}), 400

@auth_bp.route('/forgot-password', methods=['POST'])
def forgot_password():
    data = request.json
    email = data.get("email")

    try:
        reset_info = send_password_reset(email)
        return jsonify({"message": "Password reset email sent", "reset_info": reset_info})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@auth_bp.route('/totp/setup/<user_id>', methods=['GET'])
def totp_setup(user_id):
    email = request.args.get("email")
    img, secret = generate_qr_code(user_id, email)
    return send_file(img, mimetype="image/png")

@auth_bp.route('/totp/verify/<user_id>', methods=['POST'])
def totp_verify(user_id):
    data = request.json
    otp_code = data.get("otp_code")

    if verify_totp_code(user_id, otp_code):
        return jsonify({"message": "TOTP Authentication successful"})
    else:
        return jsonify({"error": "Invalid TOTP code"}), 400
