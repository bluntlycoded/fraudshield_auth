import os
import json
import firebase_admin
from firebase_admin import credentials, firestore, auth

# Retrieve Firebase credentials JSON string from the environment variable
firebase_credentials_json = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS_JSON")
if not firebase_credentials_json:
    raise ValueError("Environment variable 'GOOGLE_APPLICATION_CREDENTIALS_JSON' is not set.")

# Parse the JSON string into a Python dictionary
try:
    service_account_info = json.loads(firebase_credentials_json)
except json.JSONDecodeError as e:
    raise ValueError("Invalid JSON in 'GOOGLE_APPLICATION_CREDENTIALS_JSON': " + str(e))

# Initialize Firebase Admin SDK only if not already initialized
if not firebase_admin._apps:
    cred = credentials.Certificate(service_account_info)
    firebase_admin.initialize_app(cred)

# Initialize Firestore client
db = firestore.client()


