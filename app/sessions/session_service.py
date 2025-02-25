from app.database.firebase_config import db
from firebase_admin import firestore
def log_session(user_id, device_id, ip_address):
    db.collection("sessions").add({
        "user_id": user_id,
        "device_id": device_id,
        "ip_address": ip_address,
        "timestamp": firestore.SERVER_TIMESTAMP
    })
