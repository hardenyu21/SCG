import hashlib
import os
import base64

def task_func(password: str, salt_length: int = 8) -> str:
    # Generate a random salt
    salt = os.urandom(salt_length)
    
    # Create a new SHA-256 hash object
    hash_obj = hashlib.sha256()
    
    # Update the hash object with the salt and password
    hash_obj.update(salt + password.encode('utf-8'))
    
    # Get the digest of the hash
    digest = hash_obj.digest()
    
    # Concatenate the salt and the digest
    salted_digest = salt + digest
    
    # Encode the salted digest in base64
    base64_encoded = base64.b64encode(salted_digest)
    
    # Return the base64 encoded string
    return base64_encoded.decode('utf-8')
import unittest
import binascii
class TestCases(unittest.TestCase):
    
    def test_valid_encryption_format(self):
        encrypted = task_func("test_password")
        try:
            base64.b64decode(encrypted)
            valid = True
        except binascii.Error:
            valid = False
        self.assertTrue(valid)
    def test_varying_password_lengths(self):
        for length in [1, 5, 10, 50, 100]:
            password = "a" * length
            encrypted = task_func(password)
            self.assertTrue(isinstance(encrypted, str) and len(encrypted) > 0)
    
    def test_salt_length_effect(self):
        for salt_length in [1, 4, 8, 16]:
            encrypted = task_func("test_password", salt_length=salt_length)
            self.assertTrue(isinstance(encrypted, str) and len(encrypted) > 0)
    
    def test_special_characters_in_password(self):
        encrypted = task_func("!@#$%^&*()")
        self.assertTrue(isinstance(encrypted, str) and len(encrypted) > 0)
    
    def test_empty_password(self):
        encrypted = task_func("")
        self.assertTrue(isinstance(encrypted, str) and len(encrypted) > 0)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)