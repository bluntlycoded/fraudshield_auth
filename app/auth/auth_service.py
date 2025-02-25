import firebase_admin
from firebase_admin import credentials, auth
import os
import json

# Create a dictionary with Firebase credentials from environment variables
firebase_credentials ={
  "type": "service_account",
  "project_id": "fraudshield-authenticator",
  "private_key_id": "606ba9daadcc2158103c1b5fa2fa22630d2d8759",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCbCUs0WaWZeFVG\ngDKPoc68xBSAIzNMMh6Xvj/V9IjIZjM2RxTBpoKPmYA1Fs2UIVaLyI6thxO0L079\nr+EWcMhbSy/vRJwoq2RVRpsyWRLRLhRW7zApWKHlxV8AipA3s+K4R3uFkWteFQ4O\nGwEmqUFIA9eYbvEus6YH45HIqVUe4w5KEvFTOOtD1VSqoLSLFm3Ng2Jd6ozrMkPK\nl/u0AJYbLiBu0wdYKGAaP3Jpqdq5Nr9v+BWG4hoVrqOcwogu6P2pm0P2xpncTKb/\nt8nMggesI9LRsT9eaZFYzuYUFyG9fL1EFSROn64yBgqYDqU5COkyX5mFLpUhloVc\n4QFAH+fFAgMBAAECggEABcaD20n+DEiNf+UL44pKLE5vQRLB0qdvUlHPb1+Ye0N4\nMIZw9IHVpuNqzkKwmw5FR7HLkHu4TspDlAz2qQi/vf7mcaOWeafHQt7KSBOsMS5M\nd0Yzy7NPww9MnOi/uwN9gUXqCRP3JV5KOfMX/BVQ2qdVMCPtFVzl5RdW+Y9G6rHJ\nBvjMs9WHwvTDcFEnoj4RYg0Neo9+ecWfdOupsED0dDi5z37ZehLO2YBU2QKKpx5T\nsitEon+EZGIQUK5UQt2/siPZPOmHmbellC5TWdjqgRhyFU26Sg5bUa4N3FcRG1HU\nvEd8vQFBRrWCCGzw9YDFhkXvkeEVB/80l2JdngJxAQKBgQDLAfp2Z808Ucl4qBuM\npFq3BkFyaLIrm2uzWC9wCzm3GtiklPg4/My6ues3EfArdBMTAZrcqwQG57woys96\n2TfMoowuk8ciZ6JvHoaEjhCVPVpYv6quQcBVuXWP47GsevIw5a3KfhmYR4vDVHcT\nvX+3OkwunOJBME2LcqO9p3oWBQKBgQDDgZ4qiDNgCpdHavWRk80OB1JtqP3Nfz61\nFxXqpfZMKSrt2ajgK3iS6Os7hD/FMzX1keTNjQT3vPeroHOtQ7KPA0o0aGQY7pFV\n/e78ic7Wp5qxBXEKTvIyE5jjA4ZWKRaXOHFaOWyeG+4nBEgWcAz/p07Ytobz7SZa\neB3T12N2wQKBgGkSHRArqY4OxrgsShYA+vK/yh/tEEqBprysZ+EV7klXG8oTUGYu\nccgzcgqOvj+/VCACNKUB3pO0XS6/yaNLyhWgC+4PjoHAIdJhej4hSXP0zU4h5bVL\nUsELvE09DDi5aaDlP44OtjCa1zvB+9+7tN6gzc1SZchXt8r1CsqeZBIBAoGBAL4Z\n0h7PMw1nHvQdx8yXJ+NFMVxZ3vgri2Dwoqn4WEZ0HT8Lzw6yllpbSygjDxMEGarA\nAvfv8G2n/DeRHAnU8tHmxAeznek0SHOSKAi9Qzcr39nTTbhVTWFt9tJ+wegTqdi+\n1FGD1t7ij662lhXjPHB2Uc+dpBmZdhqwA2jSXe/BAoGBALeteuncKqpltD0J43hq\n3XXEtyUXzXmV8PqVS1XBBTpX6N9b4OCorBkQWZ5teZ6HAnfzdfPkayyA0ZEa4H8d\n38eSTNCgS9mtMa33NBObPpnK3XeOGJsuXlnnfSUxwI7IJtHGLLUsTxH1cylS3VVw\n4ZMoOXnN43O6BqILVKTJppSL\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-fbsvc@fraudshield-authenticator.iam.gserviceaccount.com",
  "client_id": "115231048817153197154",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-fbsvc%40fraudshield-authenticator.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}



# Convert dictionary to Firebase credential object
cred = credentials.Certificate(firebase_credentials)

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
