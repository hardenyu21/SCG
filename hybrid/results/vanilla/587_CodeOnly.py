import rsa
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from base64 import b64encode

def task_func(file_path):
    # Generate RSA keys
    (public_key, private_key) = rsa.newkeys(2048)

    # Read the file to be encrypted
    with open(file_path, 'rb') as file:
        file_data = file.read()

    # Generate a random AES key
    aes_key = os.urandom(32)  # 256-bit key

    # Encrypt the file using AES
    iv = os.urandom(16)  # AES block size is 16 bytes
    cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(file_data) + padder.finalize()
    encrypted_file_data = encryptor.update(padded_data) + encryptor.finalize()

    # Save the encrypted file
    encrypted_file_name = f"{os.path.splitext(file_path)[0]}_encrypted.bin"
    with open(encrypted_file_name, 'wb') as encrypted_file:
        encrypted_file.write(iv + encrypted_file_data)  # Prepend IV for decryption

    # Encrypt the AES key using the RSA public key
    encrypted_aes_key = rsa.encrypt(aes_key, public_key)

    # Save the encrypted AES key
    encrypted_key_file_name = f"{os.path.splitext(file_path)[0]}_encrypted_key.bin"
    with open(encrypted_key_file_name, 'wb') as encrypted_key_file:
        encrypted_key_file.write(encrypted_aes_key)

    return public_key, encrypted_file_name, encrypted_key_file_name

# Example usage:
# public_key, encrypted_file, encrypted_key_file = task_func('example.txt')
# print(f"Public Key: {public_key}")
# print(f"Encrypted File: {encrypted_file}")
# print(f"Encrypted AES Key File: {encrypted_key_file}")