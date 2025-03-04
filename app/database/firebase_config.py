import firebase_admin
from firebase_admin import credentials, firestore, auth
import os
FIREBASE_CREDENTIALS_PATH = "../auth/firebase_credentials.json"
if not firebase_admin._apps:
    cred = credentials.Certificate(FIREBASE_CREDENTIALS_PATH)
    firebase_admin.initialize_app(cred)
db = firestore.client()
