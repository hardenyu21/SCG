import json
import random
import hashlib
from datetime import datetime

def task_func(utc_datetime, salt='salt', password_length=10, seed=0):
    # Validate inputs
    if not isinstance(utc_datetime, datetime):
        raise ValueError("utc_datetime must be a datetime object.")
    if not isinstance(salt, str):
        raise ValueError("salt must be a string.")
    
    # Set random seed for reproducibility
    random.seed(seed)
    
    # Generate a random lowercase alphanumeric password
    characters = 'abcdefghijklmnopqrstuvwxyz0123456789'
    password = ''.join(random.choice(characters) for _ in range(password_length))
    
    # Create the string to hash: password + salt + utc_datetime string representation
    datetime_str = utc_datetime.isoformat()
    hash_input = password + salt + datetime_str
    
    # Hash the input using SHA-256
    hash_object = hashlib.sha256(hash_input.encode())
    hashed_password = hash_object.hexdigest()
    
    # Encode the hashed password as a JSON string
    json_encoded_password = json.dumps(hashed_password)
    
    return json_encoded_password