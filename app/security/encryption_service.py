from cryptography.fernet import Fernet
key = Fernet.generate_key()
cipher_suite = Fernet(key)
def encrypt(data):
    return cipher_suite.encrypt(data.encode()).decode()
def decrypt(token):
    return cipher_suite.decrypt(token.encode()).decode()
