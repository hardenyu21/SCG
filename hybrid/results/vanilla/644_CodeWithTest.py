import hashlib
import base64
import os
from cryptography.fernet import Fernet

def task_func(filename, data, password):
    # Generate a key from the password
    password_hash = hashlib.sha256(password.encode()).digest()
    key = base64.urlsafe_b64encode(password_hash[:32])
    
    # Create a Fernet object with the key
    cipher_suite = Fernet(key)
    
    # Encrypt the data
    encrypted_data = cipher_suite.encrypt(data.encode())
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    # Write the encrypted data to the file
    with open(filename, 'wb') as file:
        file.write(encrypted_data)
    
    # Return the encrypted string
    return encrypted_data.decode()

# Example usage:
# encrypted_string = task_func('path/to/encrypted_file.txt', 'Hello, World!', 'my_secure_password')
# print(encrypted_string)
import unittest
import os
import shutil
OUTPUT_DIR = './output'
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)
class TestCases(unittest.TestCase):
    def tearDown(self):
        """Clean up any files created during the tests."""
        # Check and remove the expected file if it exists
        # if os.path.exists(FILE_PATH):
        #     os.remove(FILE_PATH)
        if os.path.exists(OUTPUT_DIR):
            shutil.rmtree(OUTPUT_DIR)
    def test_case_1(self):
        # Testing basic encryption and file write
        file1 = os.path.join(OUTPUT_DIR, 'test1.txt')
        encrypted = task_func(file1, 'Hello, World!', 'password123')
        with open(file1, 'r') as f:
            file_content = f.read()
        self.assertEqual(encrypted, file_content)
        
    def test_case_2(self):
        # Testing with different data and password
        file2 = os.path.join(OUTPUT_DIR, 'test2.txt')
        encrypted = task_func(file2, 'OpenAI', 'secret')
        with open(file2, 'r') as f:
            file_content = f.read()
        self.assertEqual(encrypted, file_content)
        
    def test_case_3(self):
        # Testing with special characters in data and password
        file3 = os.path.join(OUTPUT_DIR, 'test3.txt')
        data = '!@#$%^&*()_+'
        password = 'special_chars'
        encrypted = task_func(file3, data, password)
        with open(file3, 'r') as f:
            file_content = f.read()
        self.assertEqual(encrypted, file_content)
        
    def test_case_4(self):
        # Testing file creation if it doesn't exist
        file4 = os.path.join(OUTPUT_DIR, 'nonexistent_file.txt')
        if os.path.exists(file4):
            os.remove(file4)
        encrypted = task_func(file4, 'Test Data', 'pwd')
        self.assertTrue(os.path.exists(file4))
        
    def test_case_5(self):
        # Testing decryption to ensure encryption is reversible
        file5 = os.path.join(OUTPUT_DIR, 'test5.txt')
        data = 'Decryption Test'
        password = 'decrypt_pwd'
        encrypted = task_func(file5, data, password)
        
        # Decryption logic (reverse of encryption)
        key = hashlib.sha256(password.encode()).digest()
        decrypted_bytes = [byte ^ key[i % len(key)] for i, byte in enumerate(base64.b64decode(encrypted))]
        decrypted = bytes(decrypted_bytes).decode()
        
        self.assertEqual(data, decrypted)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)