import os
import pathlib
from hashlib import md5
import unicodedata

def task_func(directory):
    def normalize_filename(filename):
        # Normalize the filename to ASCII
        normalized = unicodedata.normalize('NFKD', filename)
        return ''.join(c for c in normalized if ord(c) < 128)

    def calculate_md5(file_path):
        # Calculate the MD5 hash of the file
        hash_md5 = md5()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    result = {}
    
    # Iterate over all files in the specified directory
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            normalized_name = normalize_filename(file)
            
            # Get the file size
            file_size = os.path.getsize(file_path)
            
            # Calculate the MD5 hash
            file_md5 = calculate_md5(file_path)
            
            # Store the results in the dictionary
            result[normalized_name] = {
                'Size': file_size,
                'MD5 Hash': file_md5
            }
    
    return result
import unittest
import os
import tempfile
import hashlib
class TestCases(unittest.TestCase):
    def setUp(self):
        # Setup a temporary directory with files for testing
        self.temp_dir = tempfile.TemporaryDirectory()
        self.test_file_path = os.path.join(self.temp_dir.name, "tést.txt")
        with open(self.test_file_path, "w") as file:
            file.write("Hello World")
    def test_return_type(self):
        result = task_func(self.temp_dir.name)
        self.assertIsInstance(result, dict)
    def test_file_presence(self):
        result = task_func(self.temp_dir.name)
        self.assertIn("test.txt", result)
    def test_file_size(self):
        result = task_func(self.temp_dir.name)
        self.assertEqual(result["test.txt"]["Size"], 11)
    def test_file_hash(self):
        # This test could check the MD5 hash of a known file content
        expected_hash = hashlib.md5("Hello World".encode()).hexdigest()
        result = task_func(self.temp_dir.name)
        normalized_file_name = "test.txt"
        self.assertEqual(result[normalized_file_name]["MD5 Hash"], expected_hash)
    def test_normalized_filename(self):
        # This test could check for filename normalization (ASCII conversion)
        result = task_func(self.temp_dir.name)
        expected_name = "test.txt"
        self.assertIn(expected_name, result)
        self.assertNotIn("tést.txt", result)
    def tearDown(self):
        self.temp_dir.cleanup()


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)