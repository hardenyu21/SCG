import os
import errno
import shutil

def task_func(filename, dest_dir):
    try:
        # Ensure the destination directory exists
        os.makedirs(dest_dir, exist_ok=True)
        
        # Construct the full path for the destination file
        dest_file_path = os.path.join(dest_dir, os.path.basename(filename))
        
        # Copy the file to the destination directory
        shutil.copy2(filename, dest_file_path)
        
        # Open the original file in write mode to clear its contents
        with open(filename, 'w') as file:
            file.truncate(0)
        
        # Return the absolute path to the copied file
        return os.path.abspath(dest_file_path)
    
    except OSError as e:
        # Raise an OSError if any of the file operations fail
        raise OSError(f"An error occurred: {e.strerror}") from e
import unittest
import os
import tempfile
import shutil
class TestCases(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for the tests
        self.test_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.test_dir, 'test.txt')
        with open(self.test_file, 'w') as f:
            f.write('This is a test file.')
    def tearDown(self):
        # Clean up any files created by the test
        shutil.rmtree(self.test_dir)
    def test_copy_and_erase(self):
        # Test case description:
        # This test verifies that the function copies the file to the specified
        # destination directory and that the original file's content is cleared.
        dest_dir = os.path.join(self.test_dir, 'dest')
        copied_file = task_func(self.test_file, dest_dir)
        self.assertTrue(os.path.isfile(copied_file))
        with open(self.test_file, 'r') as f:
            self.assertEqual(f.read(), '')
    def test_non_existent_dest_dir(self):
        # Test case description:
        # This test checks the function's behavior when the destination directory
        # does not exist. It is expected to create the directory and copy the file.
        dest_dir = os.path.join(self.test_dir, 'non_existent_dir')
        copied_file = task_func(self.test_file, dest_dir)
        self.assertTrue(os.path.isdir(dest_dir))
        self.assertTrue(os.path.isfile(copied_file))
    def test_overwrite_existing_file(self):
        # Test case description:
        # This test ensures that if a file with the same name exists in the destination
        # directory, it is overwritten by the copied file.
        dest_dir = os.path.join(self.test_dir, 'dest')
        os.makedirs(dest_dir, exist_ok=True)
        existing_file_path = os.path.join(dest_dir, 'test.txt')
        with open(existing_file_path, 'w') as f:
            f.write('Old content')
        copied_file = task_func(self.test_file, dest_dir)
        with open(copied_file, 'r') as f:
            self.assertEqual(f.read(), 'This is a test file.')
    def test_same_source_and_destination(self):
        # Test case description:
        # This test checks the function's response when the source and destination
        # directories are the same. An OSError is expected to be raised.
        with self.assertRaises(OSError):
            task_func(self.test_file, self.test_dir)
    def test_invalid_source_file(self):
        # Test case description:
        # This test attempts to copy from an invalid source file path, expecting
        # the function to raise a FileNotFoundError.
        with self.assertRaises(FileNotFoundError):
            task_func('/invalid/path/to/file.txt', self.test_dir)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)