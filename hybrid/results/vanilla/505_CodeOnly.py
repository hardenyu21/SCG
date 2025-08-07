import hashlib
import hmac

def task_func(secret, message):
    # Create a new HMAC object using the secret key and the SHA-256 hash function
    hmac_obj = hmac.new(secret.encode(), message.encode(), hashlib.sha256)
    # Return the HMAC signature as a hexadecimal string
    return hmac_obj.hexdigest()

# Example usage
print(task_func('mysecretkey', 'Goodbye, world!'))