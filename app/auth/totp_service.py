import pyotp
import qrcode
from io import BytesIO
from app.database.firebase_config import db
def generate_totp_secret(user_id):
    secret = pyotp.random_base32()
    db.collection("totp_secrets").document(user_id).set({"secret": secret})
    return secret
def generate_qr_code(user_id, email):
    secret = generate_totp_secret(user_id)
    totp_uri = pyotp.totp.TOTP(secret).provisioning_uri(name=email, issuer_name="FraudShield Authenticator")
    qr = qrcode.make(totp_uri)
    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer, secret
def verify_totp_code(user_id, otp_code):
    doc = db.collection("totp_secrets").document(user_id).get()
    if not doc.exists:
        return False
    secret = doc.to_dict()["secret"]
    totp = pyotp.TOTP(secret)
    return totp.verify(otp_code)
