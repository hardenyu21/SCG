import os
import hashlib
import base64

def task_func(password, PREFIX="ME", SALT_LENGTH=16):
    if SALT_LENGTH < 0:
        raise ValueError("SALT_LENGTH must be non-negative")
    
    # Generate a random salt
    salt = os.urandom(SALT_LENGTH)
    
    # Concatenate the prefix, password, and salt
    combined = PREFIX + password + salt
    
    # Hash the combined string using SHA256
    hash_object = hashlib.sha256(combined.encode('utf-8'))
    
    # Encode the hash in base64
    base64_encoded_hash = base64.b64encode(hash_object.digest()).decode('utf-8')
    
    return base64_encoded_hash