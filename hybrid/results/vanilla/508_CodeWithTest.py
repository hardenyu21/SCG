import hashlib
import os

def task_func(file_path1, file_path2):
    # Check if both files exist
    if not os.path.exists(file_path1):
        raise FileNotFoundError(f"The file {file_path1} does not exist.")
    if not os.path.exists(file_path2):
        raise FileNotFoundError(f"The file {file_path2} does not exist.")
    
    # Function to compute MD5 hash of a file
    def compute_md5(file_path):
        hash_md5 = hashlib.md5()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    
    # Compute MD5 hashes for both files
    md5_hash1 = compute_md5(file_path1)
    md5_hash2 = compute_md5(file_path2)
    
    # Compare the MD5 hashes
    return md5_hash1 == md5_hash2
import unittest
import os
class TestCases(unittest.TestCase):
    def setUp(self):
        """Set up test environment by creating test files."""
        # Create files with predefined content for testing
        with open('file1.gz', 'wb') as f:
            f.write(b'Test content for file1 and file2.')  # Identical content for file1 and file2
        with open('file2.gz', 'wb') as f:
            f.write(b'Test content for file1 and file2.')  # Identical to file1
        with open('file3.txt', 'wb') as f:
            f.write(b'Different content for file3.')  # Different content
    def tearDown(self):
        """Clean up by removing the test files after each test."""
        os.remove('file1.gz')
        os.remove('file2.gz')
        os.remove('file3.txt')
    def test_identical_files(self):
        """Test that identical files are recognized as such."""
        self.assertTrue(task_func('file1.gz', 'file2.gz'))
    def test_different_files(self):
        """Test that files with different contents are recognized as such."""
        self.assertFalse(task_func('file1.gz', 'file3.txt'))
    def test_first_file_not_exist(self):
        """Test the behavior when the first file does not exist."""
        with self.assertRaises(FileNotFoundError):
            task_func('nonexistent1.gz', 'file2.gz')
    def test_second_file_not_exist(self):
        """Test the behavior when the second file does not exist."""
        with self.assertRaises(FileNotFoundError):
            task_func('file1.gz', 'nonexistent2.txt')
    def test_both_files_not_exist(self):
        """Test the behavior when both files do not exist."""
        with self.assertRaises(FileNotFoundError):
            task_func('nonexistent1.gz', 'nonexistent2.txt')


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)