import rsa
import os
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from base64 import b64encode, b64decode

def task_func():
    # Generate RSA key pair
    (public_key, private_key) = rsa.newkeys(2048)

    # Generate a random password and nonce for AES encryption
    password = get_random_bytes(16)  # AES key size is 16 bytes
    nonce = get_random_bytes(12)     # AES GCM nonce size is 12 bytes

    # Encrypt the private key using AES-GCM
    cipher = AES.new(password, AES.MODE_GCM, nonce=nonce)
    encrypted_private_key, tag = cipher.encrypt_and_digest(private_key.save_pkcs1())

    # Generate a random number for the filename
    random_number = get_random_bytes(8).hex()
    filename = f"private_key_{random_number}.txt"

    # Save the encrypted private key to a file
    with open(filename, 'wb') as file:
        file.write(encrypted_private_key)

    # Return the public key, filename, password, and nonce
    return public_key, filename, password, nonce

# Example usage
if __name__ == "__main__":
    public_key, filename, password, nonce = task_func()
    print(f"Public Key: {public_key}")
    print(f"Encrypted Private Key Filename: {filename}")
    print(f"Encryption Password (for testing): {b64encode(password).decode()}")
    print(f"Encryption Nonce (for testing): {b64encode(nonce).decode()}")