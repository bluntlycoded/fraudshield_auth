import pyotp
SECRET_OTP_KEY = "FRAUDSHIELD_SECRET"
def generate_otp():
    totp = pyotp.TOTP(SECRET_OTP_KEY)
    return totp.now()
def verify_otp(otp):
    totp = pyotp.TOTP(SECRET_OTP_KEY)
    return totp.verify(otp)
