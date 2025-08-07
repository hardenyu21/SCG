import rsa
import os
import zipfile
from base64 import b64encode

def task_func(directory):
    # Generate RSA public and private keys
    (public_key, private_key) = rsa.newkeys(2048)

    # Create a temporary directory to store encrypted files
    temp_dir = 'encrypted_files'
    os.makedirs(temp_dir, exist_ok=True)

    # Encrypt each file in the specified directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'rb') as file:
                file_data = file.read()
                # Encrypt the file data using the public key
                encrypted_data = rsa.encrypt(file_data, public_key)
                # Encode the encrypted data in base64 to ensure it's safe to write to a file
                encoded_data = b64encode(encrypted_data).decode('utf-8')
                # Save the encrypted data to a new file in the temporary directory
                encrypted_file_path = os.path.join(temp_dir, filename + '.enc')
                with open(encrypted_file_path, 'w') as encrypted_file:
                    encrypted_file.write(encoded_data)

    # Create a zip file containing all the encrypted files
    zip_filename = 'encrypted_files.zip'
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(temp_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, temp_dir)
                zipf.write(file_path, arcname)

    # Clean up the temporary directory
    for root, dirs, files in os.walk(temp_dir, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(temp_dir)

    # Return the public key and the name of the zip file
    return public_key, zip_filename
import rsa
import os
import zipfile
from base64 import b64encode
import unittest
import tempfile
import shutil
class TestCases(unittest.TestCase):
    def setUp(self):
        # Setup a temporary directory
        self.test_dir = tempfile.mkdtemp()
    def tearDown(self):
        # Remove the directory after the test
        shutil.rmtree(self.test_dir)
        # Remove created zip file
        if os.path.exists('encrypted_files.zip'):
            os.remove('encrypted_files.zip')
    def test_return_type(self):
        # Creating test files
        for i in range(2):
            with open(os.path.join(self.test_dir, f"file{i}.txt"), 'w') as f:
                f.write("Sample content")
        pub_key, zipfile_name = task_func(self.test_dir)
        self.assertIsInstance(pub_key, rsa.PublicKey)
        self.assertIsInstance(zipfile_name, str)
    def test_zipfile_creation(self):
        # Creating test files
        for i in range(2):
            with open(os.path.join(self.test_dir, f"file{i}.txt"), 'w') as f:
                f.write("Sample content")
        _, zipfile_name = task_func(self.test_dir)
        self.assertTrue(os.path.exists(zipfile_name))
        with zipfile.ZipFile(zipfile_name, 'r') as zipf:
            self.assertEqual(len(zipf.namelist()), 2)
    def test_empty_directory(self):
        # No files created in the setup for this test
        _, zipfile_name = task_func(self.test_dir)
        with zipfile.ZipFile(zipfile_name, 'r') as zipf:
            self.assertEqual(len(zipf.namelist()), 0)
    def test_file_encryption_contents(self):
        # Creating a single test file
        test_file_path = os.path.join(self.test_dir, "test_file.txt")
        with open(test_file_path, 'w') as f:
            f.write("Sample content")
        pub_key, zipfile_name = task_func(self.test_dir)
        with zipfile.ZipFile(zipfile_name, 'r') as zipf:
            encrypted_content = zipf.read(os.path.basename(test_file_path))
            # Read the content to ensure it is encrypted and not plain text
            self.assertNotEqual(b64encode(b"Sample content").decode('utf-8'), encrypted_content)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)