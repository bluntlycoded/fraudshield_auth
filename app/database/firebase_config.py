import firebase_admin
from firebase_admin import credentials, firestore, auth
import os,json
firebase_credentials_json = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS_JSON")
if not firebase_admin._apps:
    firebase_credentials_json = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS_JSON")
service_account_info = json.loads(firebase_credentials_json)
cred = credentials.Certificate(service_account_info)
db = firestore.client()
