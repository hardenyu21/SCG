import base64
import hashlib
import os

def task_func(password, SALT_LENGTH=32):
    if password is None or password == "":
        raise ValueError("Password cannot be None or empty")
    
    # Generate a random salt
    salt = os.urandom(SALT_LENGTH)
    
    # Hash the password using PBKDF2 HMAC with SHA-256
    hashed_password = hashlib.pbkdf2_hmac(
        'sha256',  # The hash digest algorithm for HMAC
        password.encode('utf-8'),  # Convert the password to bytes
        salt,  # Provide the salt
        100000  # It is recommended to use at least 100,000 iterations of SHA-256 
    )
    
    # Base64 encode the salt and the hashed password
    encoded_salt = base64.b64encode(salt)
    encoded_hashed_password = base64.b64encode(hashed_password)
    
    return (encoded_salt, encoded_hashed_password)
import unittest
import base64
import hashlib
import os
class TestCases(unittest.TestCase):
    def decode_and_regenerate_password(self, encoded_salt, encoded_hashed_password, original_password):
        """ Helper function to decode base64 encoded salt and password, and regenerate the hashed password. """
        decoded_salt = base64.b64decode(encoded_salt)
        decoded_hashed_password = base64.b64decode(encoded_hashed_password)
        regenerated_hashed_password = hashlib.pbkdf2_hmac('sha256', original_password.encode(), decoded_salt, 100000)
        return regenerated_hashed_password, decoded_hashed_password
    def test_case_1(self):
        """ Testing with a simple password """
        salt, hashed_password = task_func('password123')
        self.assertTrue(isinstance(salt, bytes) and isinstance(hashed_password, bytes))
        regenerated, original = self.decode_and_regenerate_password(salt, hashed_password, 'password123')
        self.assertEqual(regenerated, original)
    def test_case_2(self):
        """ Testing with a password containing special characters """
        salt, hashed_password = task_func('p@ssw0rd$%^&*')
        self.assertTrue(isinstance(salt, bytes) and isinstance(hashed_password, bytes))
        regenerated, original = self.decode_and_regenerate_password(salt, hashed_password, 'p@ssw0rd$%^&*')
        self.assertEqual(regenerated, original)
    def test_case_3(self):
        """ Testing with a long password """
        long_password = 'a' * 1000
        salt, hashed_password = task_func(long_password)
        self.assertTrue(isinstance(salt, bytes) and isinstance(hashed_password, bytes))
        regenerated, original = self.decode_and_regenerate_password(salt, hashed_password, long_password)
        self.assertEqual(regenerated, original)
    def test_case_4(self):
        """ Testing with a short password """
        short_password = 'a'
        salt, hashed_password = task_func(short_password)
        self.assertTrue(isinstance(salt, bytes) and isinstance(hashed_password, bytes))
        regenerated, original = self.decode_and_regenerate_password(salt, hashed_password, short_password)
        self.assertEqual(regenerated, original)
    def test_case_5(self):
        """ Testing with a password that is a number """
        number_password = '1234567890'
        salt, hashed_password = task_func(number_password)
        self.assertTrue(isinstance(salt, bytes) and isinstance(hashed_password, bytes))
        regenerated, original = self.decode_and_regenerate_password(salt, hashed_password, number_password)
        self.assertEqual(regenerated, original)
    def test_invalid_input(self):
        """ Testing with invalid input such as None or empty string """
        with self.assertRaises(ValueError):
            task_func(None)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)