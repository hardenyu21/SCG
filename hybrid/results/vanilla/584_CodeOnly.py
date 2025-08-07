import rsa
import urllib.request
from hashlib import sha256

def task_func(url):
    try:
        # Generate RSA public and private keys
        (public_key, private_key) = rsa.newkeys(2048)

        # Retrieve content from the specified URL
        with urllib.request.urlopen(url) as response:
            if response.status != 200:
                raise ValueError(f"HTTP error: {response.status}")
            content = response.read()

        # Calculate the SHA256 hash of the content
        hashed_content = sha256(content).digest()

        # Sign the hash with the private key
        try:
            signed_hash = rsa.sign(hashed_content, private_key, 'SHA-256')
        except rsa.pkcs1.VerificationError as e:
            raise rsa.pkcs1.VerificationError("Failed to sign the hash with the RSA private key.") from e

        # Convert the signed hash to a hexadecimal string
        signed_hash_hex = signed_hash.hex()

        return public_key, signed_hash_hex, hashed_content

    except urllib.error.URLError as e:
        raise urllib.error.URLError("The server is not reachable.") from e
    except ValueError as e:
        raise ValueError("There's an issue reaching the server or the server returned an HTTP error.") from e