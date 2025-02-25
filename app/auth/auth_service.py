from firebase_admin import auth
def create_user(email, password):
    user = auth.create_user(email=email, password=password)
    return {"uid": user.uid, "email": user.email}
def send_password_reset(email):
    link = auth.generate_password_reset_link(email)
    return {"reset_link": link}
