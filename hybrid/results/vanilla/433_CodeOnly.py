import base64
import hashlib
import hmac
import binascii

def task_func(s, signature, secret_key):
    try:
        # Decode the base64-encoded message
        message = base64.b64decode(s)
        
        # Compute the HMAC SHA-1 hash of the message using the secret key
        computed_hmac = hmac.new(secret_key.encode(), message, hashlib.sha1)
        
        # Compare the computed HMAC with the provided signature
        # The provided signature should be in hexadecimal format
        return hmac.compare_digest(computed_hmac.hexdigest(), signature)
    except (binascii.Error, TypeError):
        # Handle decoding errors or type mismatches
        return False

# Example usage
print(task_func('SGVsbG8gV29ybGQ=', 'incorrect_signature', 'my_secret_key'))  # Output: False