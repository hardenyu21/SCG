import difflib
import gzip

def task_func(file_path1, file_path2):
    # Read the contents of the first gzip file
    with gzip.open(file_path1, 'rt', encoding='utf-8') as f1:
        content1 = f1.readlines()
    
    # Read the contents of the second gzip file
    with gzip.open(file_path2, 'rt', encoding='utf-8') as f2:
        content2 = f2.readlines()
    
    # Use difflib to compute the differences
    diff = difflib.unified_diff(content1, content2, fromfile=file_path1, tofile=file_path2, lineterm='')
    
    # Join the differences into a single string
    diff_str = '\n'.join(diff)
    
    return diff_str
import unittest
import os
class TestCases(unittest.TestCase):
    def setUp(self):
        """Set up test environment by creating test gzip files with known content."""
        with gzip.open('file1.gz', 'wt') as f:
            f.write("This is a test file.\n")
        with gzip.open('file2.gz', 'wt') as f:
            f.write("This is a different test file.\n")
    def tearDown(self):
        """Clean up by removing the test gzip files."""
        os.remove('file1.gz')
        os.remove('file2.gz')
    def test_identical_files(self):
        """Test that the function returns an empty string for identical files."""
        self.assertEqual(task_func('file1.gz', 'file1.gz'), '')
    def test_different_files(self):
        """Test that the function identifies differences between two files."""
        result = task_func('file1.gz', 'file2.gz')
        self.assertTrue("different" in result)
    def test_first_file_not_exist(self):
        """Test that the function raises FileNotFoundError if the first file does not exist."""
        with self.assertRaises(FileNotFoundError):
            task_func('nonexistent1.gz', 'file2.gz')
    def test_second_file_not_exist(self):
        """Test that the function raises FileNotFoundError if the second file does not exist."""
        with self.assertRaises(FileNotFoundError):
            task_func('file1.gz', 'nonexistent2.gz')
    def test_both_files_not_exist(self):
        """Test that the function raises FileNotFoundError if both files do not exist."""
        with self.assertRaises(FileNotFoundError):
            task_func('nonexistent1.gz', 'nonexistent2.gz')


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)