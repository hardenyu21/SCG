import rsa
from cryptography.fernet import Fernet
from base64 import b64encode

def task_func(file_path):
    # Generate RSA public and private keys
    (public_key, private_key) = rsa.newkeys(2048)

    # Generate a Fernet key
    fernet_key = Fernet.generate_key()
    cipher_suite = Fernet(fernet_key)

    # Read the contents of the specified file
    with open(file_path, 'rb') as file:
        file_contents = file.read()

    # Encrypt the file contents using Fernet
    encrypted_file_contents = cipher_suite.encrypt(file_contents)

    # Encrypt the Fernet key using the RSA public key
    encrypted_fernet_key = rsa.encrypt(fernet_key, public_key)

    # Save the encrypted file contents to a new file
    encrypted_file_path = file_path + '.encrypted'
    with open(encrypted_file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_file_contents)

    # Save the encrypted Fernet key to a new file
    encrypted_key_file_path = file_path + '.key.encrypted'
    with open(encrypted_key_file_path, 'wb') as encrypted_key_file:
        encrypted_key_file.write(encrypted_fernet_key)

    # Return the public key, encrypted file path, and encrypted key file path
    return public_key, encrypted_file_path, encrypted_key_file_path

# Example usage:
# public_key, encrypted_file, encrypted_key_file = task_func('example.txt')
# print("Public Key:", public_key)
# print("Encrypted File:", encrypted_file)
# print("Encrypted Key File:", encrypted_key_file)
import unittest
from cryptography.fernet import Fernet
import os
import rsa
class TestCases(unittest.TestCase):
    def setUp(self):
        # Setup a test file
        self.test_file = 'test_file.txt'
        with open(self.test_file, 'w') as f:
            f.write("This is a test file.")
    def test_file_encryption(self):
        pub_key, encrypted_file, _ = task_func(self.test_file)
        self.assertTrue(os.path.exists(encrypted_file))
    def test_encrypted_key_file_creation(self):
        pub_key, _, encrypted_key_file = task_func(self.test_file)
        self.assertTrue(os.path.exists(encrypted_key_file))
    def test_public_key_type(self):
        pub_key, _, _ = task_func(self.test_file)
        self.assertIsInstance(pub_key, rsa.PublicKey)
    def test_encrypted_file_size(self):
        _, encrypted_file, _ = task_func(self.test_file)
        original_size = os.path.getsize(self.test_file)
        encrypted_size = os.path.getsize(encrypted_file)
        self.assertTrue(encrypted_size > original_size)
    def test_non_existent_file(self):
        with self.assertRaises(FileNotFoundError):
            task_func("non_existent_file.txt")
    def tearDown(self):
        # Clean up created files
        os.remove(self.test_file)
        encrypted_file = self.test_file + '.encrypted'
        if os.path.exists(encrypted_file):
            os.remove(encrypted_file)
        if os.path.exists('fernet_key.encrypted'):
            os.remove('fernet_key.encrypted')


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)