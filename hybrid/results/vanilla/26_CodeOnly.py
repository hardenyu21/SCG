import base64
from cryptography.fernet import Fernet

def task_func(message, encryption_key):
    # Ensure the message is in bytes
    if isinstance(message, str):
        message = message.encode('utf-8')
    
    # Create a Fernet object with the provided encryption key
    fernet = Fernet(encryption_key)
    
    # Encrypt the message
    encrypted_message = fernet.encrypt(message)
    
    # Encode the encrypted message using base64
    base64_encoded_message = base64.b64encode(encrypted_message)
    
    # Convert the base64 bytes to a string and return
    return base64_encoded_message.decode('utf-8')

# Example usage:
# key = Fernet.generate_key()
# encrypted_message = task_func("Hello, World!", key)
# print(encrypted_message)