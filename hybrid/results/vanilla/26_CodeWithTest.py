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
import unittest
import base64
from cryptography.fernet import Fernet
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test with a basic message and a valid encryption key.
        result = task_func('Hello, World!', '01234567890123456789012345678901')
        self.assertIsInstance(result, str)
        self.assertNotEqual(result, 'Hello, World!')
    def test_case_2(self):
        # Test with an empty message and a valid encryption key.
        result = task_func('', '01234567890123456789012345678901')
        self.assertIsInstance(result, str)
        self.assertNotEqual(result, '')
    def test_case_3(self):
        # Test with a numeric message and a valid encryption key.
        result = task_func('1234567890', '01234567890123456789012345678901')
        self.assertIsInstance(result, str)
        self.assertNotEqual(result, '1234567890')
    def test_case_4(self):
        # Test with a long message and a valid encryption key.
        long_message = 'A' * 500
        result = task_func(long_message, '01234567890123456789012345678901')
        self.assertIsInstance(result, str)
        self.assertNotEqual(result, long_message)
    def test_case_5(self):
        # Test with a basic message and an incorrectly formatted encryption key.
        with self.assertRaises(ValueError):
            task_func('Hello, World!', '0123456789')
    def test_case_6(self):
        # Test with a non-base64 but correct length key.
        with self.assertRaises(Exception):
            task_func('Hello, World!', '01234567890123456789012345678901'*2)  # Not base64-encoded


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)