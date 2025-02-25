from app.database.firebase_config import db
def log_event(event, details):
    db.collection("logs").add({
        "event": event,
        "details": details
    })
