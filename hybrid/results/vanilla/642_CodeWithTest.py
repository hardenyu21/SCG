import os
import hashlib
import re

OUTPUT_DIR = './output'

def task_func(directory: str, pattern: str = r"(?<!Distillr)\\AcroTray\.exe") -> dict:
    # Compile the regex pattern for matching
    regex = re.compile(pattern)
    
    # Dictionary to store file paths and their SHA256 hashes
    file_hashes = {}
    
    # Walk through the directory
    for root, _, files in os.walk(directory):
        for file in files:
            # Construct the full file path
            file_path = os.path.join(root, file)
            
            # Check if the file path matches the regex pattern
            if regex.search(file_path):
                # Compute the SHA256 hash of the file's content
                sha256_hash = hashlib.sha256()
                try:
                    with open(file_path, 'rb') as f:
                        # Read and update hash string value in blocks of 4K
                        for byte_block in iter(lambda: f.read(4096), b""):
                            sha256_hash.update(byte_block)
                    # Store the hash in the dictionary
                    file_hashes[file_path] = sha256_hash.hexdigest()
                except Exception as e:
                    print(f"Error reading file {file_path}: {e}")
    
    return file_hashes
import unittest
import tempfile
import shutil
import os
class TestCases(unittest.TestCase):
    def setUp(self):
        self.test_dir = OUTPUT_DIR
        if not os.path.exists(self.test_dir):
            os.makedirs(self.test_dir)
        # Create a test file within the test_dir
        self.test_file = os.path.join(self.test_dir, "AcroTray.exe")
        with open(self.test_file, 'wb') as f:
            f.write(b"Dummy content for testing.")
    def tearDown(self):
        # Clean up by removing the test directory and its contents
        shutil.rmtree(self.test_dir, ignore_errors=True)
    def test_matching_file(self):
        """Ensure the method correctly identifies and hashes a matching file."""
        # Use the directory, not the file path, and adjust the pattern if necessary.
        result = task_func(self.test_dir, r"AcroTray\.exe$")
        # Verify that the file's full path is included in the results
        self.assertIn(self.test_file, result.keys(), "The file should be found and hashed.")
        # Optionally, verify the correctness of the hash value for added robustness.
        # Compute the expected hash for comparison
        with open(self.test_file, 'rb') as file:
            data = file.read()
            expected_hash = hashlib.sha256(data).hexdigest()
        self.assertEqual(result[self.test_file], expected_hash, "The hash value should match the expected hash.")
    def test_no_matching_file(self):
        """Test directory with no files matching the pattern."""
        no_match_dir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, no_match_dir)  # Ensure cleanup
        result = task_func(no_match_dir)
        self.assertEqual(len(result), 0)
    def test_empty_directory(self):
        """Test an empty directory."""
        empty_dir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, empty_dir)  # Ensure cleanup
        result = task_func(empty_dir)
        self.assertEqual(len(result), 0)
    def test_hash_correctness(self):
        """Verify that the SHA256 hash is correctly computed."""
        # Adjust the call to search within the test directory and specify a pattern that matches the test file
        pattern = "AcroTray\.exe$"  # Simplified pattern to match the filename directly
        result = task_func(self.test_dir, pattern)
        # Construct the expected key as it would appear in the result
        expected_key = self.test_file
        # Ensure the file was matched and the hash is present in the results
        self.assertIn(expected_key, result)
        hash_value = result[expected_key]
        # Compute the expected hash for comparison
        with open(self.test_file, 'rb') as f:
            data = f.read()
            expected_hash = hashlib.sha256(data).hexdigest()
        self.assertEqual(hash_value, expected_hash)
    def test_custom_pattern(self):
        """Test functionality with a custom pattern that does not match any file."""
        custom_pattern = r"non_matching_pattern\.exe$"
        result = task_func(self.test_file, custom_pattern)
        self.assertEqual(len(result), 0)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)