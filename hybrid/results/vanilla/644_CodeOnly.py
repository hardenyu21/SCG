import hashlib
import base64
import os
from cryptography.fernet import Fernet

def task_func(filename, data, password):
    # Generate a key from the password
    password_hash = hashlib.sha256(password.encode()).digest()
    key = base64.urlsafe_b64encode(password_hash[:32])
    
    # Create a Fernet object with the key
    cipher_suite = Fernet(key)
    
    # Encrypt the data
    encrypted_data = cipher_suite.encrypt(data.encode())
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    # Write the encrypted data to the file
    with open(filename, 'wb') as file:
        file.write(encrypted_data)
    
    # Return the encrypted string
    return encrypted_data.decode()

# Example usage:
# encrypted_string = task_func('path/to/encrypted_file.txt', 'Hello, World!', 'my_secure_password')
# print(encrypted_string)