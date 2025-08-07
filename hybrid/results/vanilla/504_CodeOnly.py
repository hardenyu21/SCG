import hashlib
import rsa
import base64

def task_func(file_path):
    # Read the contents of the file
    with open(file_path, 'rb') as file:
        file_contents = file.read()

    # Hash the file contents using SHA-256
    sha256_hash = hashlib.sha256(file_contents).digest()

    # Load the private RSA key from 'private.pem'
    with open('private.pem', 'rb') as private_key_file:
        private_key = rsa.PrivateKey.load_pkcs1(private_key_file.read())

    # Sign the hash with the private RSA key
    signed_hash = rsa.sign(sha256_hash, private_key, 'SHA-256')

    # Encode the signed hash in base64
    base64_encoded_signed_hash = base64.b64encode(signed_hash).decode('utf-8')

    return base64_encoded_signed_hash