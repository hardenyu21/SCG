import os
import hashlib
import json
from pathlib import Path

def task_func(directory: str) -> str:
    def calculate_sha256(file_path: str) -> str:
        """Calculate the SHA256 hash of a file."""
        sha256_hash = hashlib.sha256()
        with open(file_path, "rb") as f:
            # Read and update hash string value in blocks of 4K
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()

    hashes = {}
    # Walk through all directories and files in the specified directory
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, directory)
            hashes[relative_path] = calculate_sha256(file_path)

    # Define the path for the JSON file
    json_file_path = os.path.join(directory, 'hashes.json')
    
    # Write the hashes to the JSON file
    with open(json_file_path, 'w') as json_file:
        json.dump(hashes, json_file, indent=4)

    # Return the absolute path of the JSON file
    return os.path.abspath(json_file_path)
import unittest
import os
import hashlib
import json
from pathlib import Path
import tempfile
class TestCases(unittest.TestCase):
    def setUp(self):
        # Creating a temporary directory for testing
        self.test_dir = tempfile.mkdtemp()
    def tearDown(self):
        # Cleaning up the temporary directory
        for root, dirs, files in os.walk(self.test_dir, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(self.test_dir)
    def test_empty_directory(self):
        # Testing with an empty directory
        json_file = task_func(self.test_dir)
        self.assertTrue(os.path.exists(json_file))
        with open(json_file, 'r') as f:
            data = json.load(f)
            self.assertEqual(data, {})
    def test_single_file(self):
        # Testing with a directory containing a single file
        filepath = os.path.join(self.test_dir, 'file1.txt')
        with open(filepath, 'w') as f:
            f.write("Hello, world!")
        json_file = task_func(self.test_dir)
        self.assertTrue(os.path.exists(json_file))
        with open(json_file, 'r') as f:
            data = json.load(f)
            self.assertIn(filepath, data.keys())
    def test_multiple_files(self):
        # Testing with a directory containing multiple files
        files_content = {'file2.txt': "Hello again!", 'file3.txt': "Goodbye!"}
        filepaths = {}
        for filename, content in files_content.items():
            filepath = os.path.join(self.test_dir, filename)
            filepaths[filepath] = content
            with open(filepath, 'w') as f:
                f.write(content)
        json_file = task_func(self.test_dir)
        self.assertTrue(os.path.exists(json_file))
        with open(json_file, 'r') as f:
            data = json.load(f)
            for filepath in filepaths.keys():
                self.assertIn(filepath, data.keys())
    def test_nested_directories(self):
        # Testing with a directory containing nested subdirectories and files
        sub_dir = os.path.join(self.test_dir, 'sub_dir')
        filepath = os.path.join(sub_dir, 'file4.txt')
        Path(sub_dir).mkdir(parents=True, exist_ok=True)
        with open(filepath, 'w') as f:
            f.write("Nested file content!")
        json_file = task_func(self.test_dir)
        self.assertTrue(os.path.exists(json_file))
        with open(json_file, 'r') as f:
            data = json.load(f)
            self.assertIn(filepath, data.keys())
    def test_correct_hash(self):
        # Testing if the computed hash is correct
        filepath = os.path.join(self.test_dir, 'file5.txt')
        with open(filepath, 'w') as f:
            f.write("Check hash!")
        json_file = task_func(self.test_dir)
        self.assertTrue(os.path.exists(json_file))
        with open(filepath, 'rb') as f:
            bytes = f.read()
            expected_hash = hashlib.sha256(bytes).hexdigest()
        with open(json_file, 'r') as f:
            data = json.load(f)
            self.assertEqual(data[filepath], expected_hash)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)