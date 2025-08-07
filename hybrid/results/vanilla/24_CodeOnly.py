import base64
import hashlib
import os

def task_func(password, SALT_LENGTH=32):
    if password is None or password == "":
        raise ValueError("Password cannot be None or empty")
    
    # Generate a random salt
    salt = os.urandom(SALT_LENGTH)
    
    # Hash the password using PBKDF2 HMAC with SHA-256
    hashed_password = hashlib.pbkdf2_hmac(
        'sha256',  # The hash digest algorithm for HMAC
        password.encode('utf-8'),  # Convert the password to bytes
        salt,  # Provide the salt
        100000  # It is recommended to use at least 100,000 iterations of SHA-256 
    )
    
    # Base64 encode the salt and the hashed password
    encoded_salt = base64.b64encode(salt)
    encoded_hashed_password = base64.b64encode(hashed_password)
    
    return (encoded_salt, encoded_hashed_password)