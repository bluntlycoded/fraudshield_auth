import firebase_admin
from firebase_admin import credentials, auth
import os
import json

# Load Firebase credentials from environment variable (Railway)
firebase_credentials = os.getenv("GOOGLE_APPLICATION_CREDENTIALS_JSON")

if firebase_credentials:
    # Convert the JSON string back into a dictionary
    cred_dict = json.loads(firebase_credentials)
    cred = credentials.Certificate(cred_dict)
else:
    raise ValueError("Firebase credentials are missing. Make sure GOOGLE_APPLICATION_CREDENTIALS_JSON is set.")

# Ensure Firebase is initialized only once
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

def create_user(email, password):
    """ Creates a new user with Firebase Authentication """
    try:
        user = auth.create_user(email=email, password=password)
        return {"uid": user.uid, "email": user.email}
    except Exception as e:
        return {"error": str(e)}

def send_password_reset(email):
    """ Sends a password reset email using Firebase Auth """
    try:
        link = auth.generate_password_reset_link(email)
        return {"reset_link": link}
    except Exception as e:
        return {"error": str(e)}
