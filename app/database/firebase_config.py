import firebase_admin
from firebase_admin import credentials, firestore, auth
import os
firebase_credentials_json = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS_JSON")
if not firebase_admin._apps:
    cred = credentials.Certificate(firebase_credentials_json)
    firebase_admin.initialize_app(cred)
db = firestore.client()
