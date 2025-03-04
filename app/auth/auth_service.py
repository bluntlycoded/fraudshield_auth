import os
import json
import firebase_admin
from firebase_admin import credentials, auth

# Retrieve Firebase credentials from the environment variable
firebase_credentials_json = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS_JSON")
if not firebase_credentials_json:
    raise ValueError("Environment variable 'GOOGLE_APPLICATION_CREDENTIALS_JSON' is not set.")

# Parse the JSON string into a Python dictionary
try:
    service_account_info = json.loads(firebase_credentials_json)
except json.JSONDecodeError as e:
    raise ValueError("Invalid JSON in 'GOOGLE_APPLICATION_CREDENTIALS_JSON': " + str(e))

# Initialize Firebase Admin SDK only once
if not firebase_admin._apps:
    cred = credentials.Certificate(service_account_info)
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
