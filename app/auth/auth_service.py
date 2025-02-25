import firebase_admin
from firebase_admin import credentials, auth
import json
import os

# If running on Railway, load credentials from env variable
firebase_credentials = os.getenv("GOOGLE_APPLICATION_CREDENTIALS_JSON")

if firebase_credentials:
    cred_dict = json.loads(firebase_credentials)  # Convert JSON string back to dict
    cred = credentials.Certificate(cred_dict)
else:
    cred = credentials.Certificate("firebase_credentials.json")  # Local file

# Initialize Firebase only once
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

def create_user(email, password):
    try:
        user = auth.create_user(email=email, password=password)
        return {"uid": user.uid, "email": user.email}
    except Exception as e:
        return {"error": str(e)}
