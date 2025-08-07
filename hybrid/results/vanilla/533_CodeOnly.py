import numpy as np
import secrets
import hashlib
import base64

def task_func(num, from_base, to_base, alphabet):
    # Validate bases
    if from_base < 2 or to_base < 2:
        raise ValueError("Base must be at least 2.")
    
    # Validate number format
    try:
        int(num, from_base)
    except ValueError:
        raise ValueError(f"Number '{num}' contains invalid characters for base {from_base}.")
    
    # Convert number from one base to another
    converted_num = int(num, from_base)
    converted_num_str = np.base_repr(converted_num, base=to_base)
    
    # Generate a random salt
    salt = secrets.token_bytes(16)
    
    # Create the message to hash
    message = (converted_num_str + salt.decode()).encode()
    
    # Hash the message using SHA-256
    hash_object = hashlib.sha256(message)
    hash_bytes = hash_object.digest()
    
    # Encode the hash in base64 using the custom alphabet
    base64_encoded = base64.b64encode(hash_bytes, alphabet.encode()).decode()
    
    return base64_encoded, salt

# Example usage
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
result1, salt1 = task_func('FF', 16, 8, alphabet)
result2, salt2 = task_func('FF', 16, 8, alphabet)
print(result1 != result2)  # Should print True