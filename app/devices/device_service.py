from app.database.firebase_config import db
def register_device(user_id, device_id, device_name):
    db.collection("devices").document(device_id).set({
        "user_id": user_id,
        "device_name": device_name,
        "trusted": False
    })
def mark_device_as_trusted(device_id):
    db.collection("devices").document(device_id).update({"trusted": True})
