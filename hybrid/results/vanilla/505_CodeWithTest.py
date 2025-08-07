import hashlib
import hmac

def task_func(secret, message):
    # Create a new HMAC object using the secret key and the SHA-256 hash function
    hmac_obj = hmac.new(secret.encode(), message.encode(), hashlib.sha256)
    # Return the HMAC signature as a hexadecimal string
    return hmac_obj.hexdigest()

# Example usage
print(task_func('mysecretkey', 'Goodbye, world!'))
import unittest
class TestCases(unittest.TestCase):
    def test_hmac_signature_length(self):
        signature = task_func('secretkey', 'Hello, world!')
        self.assertEqual(len(signature), 64)
    def test_hmac_signature_different_messages(self):
        sig1 = task_func('secretkey', 'Hello, world!')
        sig2 = task_func('secretkey', 'Goodbye, world!')
        self.assertNotEqual(sig1, sig2)
    def test_hmac_signature_same_message_different_keys(self):
        sig1 = task_func('key1', 'Hello, world!')
        sig2 = task_func('key2', 'Hello, world!')
        self.assertNotEqual(sig1, sig2)
    def test_hmac_signature_empty_message(self):
        signature = task_func('secretkey', '')
        self.assertEqual(len(signature), 64)
    def test_hmac_signature_empty_key(self):
        signature = task_func('', 'Hello, world!')
        self.assertEqual(len(signature), 64)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)