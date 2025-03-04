import firebase_admin
from firebase_admin import credentials, auth

# Ensure Firebase is initialized only once
if not firebase_admin._apps:
    cred = credentials.Certificate("firebase_credentials.json")
    firebase_admin.initialize_app(cred)

def create_user(email, password):
    try:
        user = auth.create_user(email=email, password=password)
        return {"uid": user.uid, "email": user.email}
    except Exception as e:
        return {"error": str(e)}

def send_password_reset(email):
    try:
        link = auth.generate_password_reset_link(email)
        return {"reset_link": link}
    except Exception as e:
        return {"error": str(e)}