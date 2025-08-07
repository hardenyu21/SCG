import hashlib
import os
import base64

def task_func(password: str, salt_length: int = 8) -> str:
    # Generate a random salt
    salt = os.urandom(salt_length)
    
    # Create a new SHA-256 hash object
    hash_obj = hashlib.sha256()
    
    # Update the hash object with the salt and password
    hash_obj.update(salt + password.encode('utf-8'))
    
    # Get the digest of the hash
    digest = hash_obj.digest()
    
    # Concatenate the salt and the digest
    salted_digest = salt + digest
    
    # Encode the salted digest in base64
    base64_encoded = base64.b64encode(salted_digest)
    
    # Return the base64 encoded string
    return base64_encoded.decode('utf-8')