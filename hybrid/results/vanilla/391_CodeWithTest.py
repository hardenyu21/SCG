import os
import glob
import shutil

def task_func(directory, archive_dir='archive'):
    # Ensure the archive directory exists
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)

    # Find all JSON files in the given directory
    json_files = glob.glob(os.path.join(directory, '*.json'))
    
    # Initialize a list to store error messages
    error_messages = []

    # Iterate over each JSON file
    for file_path in json_files:
        try:
            # Construct the destination path
            file_name = os.path.basename(file_path)
            destination_path = os.path.join(archive_dir, file_name)
            
            # Move the file to the archive directory
            shutil.move(file_path, destination_path)
        except Exception as e:
            # If an error occurs, add a message to the error list
            error_messages.append(f"Failed to move {file_path}: {str(e)}")

    # Determine if all files were successfully moved
    all_files_moved = len(error_messages) == 0

    # Return the result as a tuple
    return (all_files_moved, error_messages)
import unittest
import doctest
class TestCases(unittest.TestCase):
    def setUp(self):
        # Create a test directory with some JSON files and some other file types
        os.makedirs('test_data', exist_ok=True)
        with open('test_data/test1.json', 'w') as f:
            f.write('{}')
        with open('test_data/test2.json', 'w') as f:
            f.write('{}')
        with open('test_data/test.txt', 'w') as f:
            f.write('Hello')
        # Create a different archive directory for one of the tests
        os.makedirs('custom_archive', exist_ok=True)
        os.makedirs('archive', exist_ok=True)
    def tearDown(self):
        # Clean up test directories and files
        shutil.rmtree('test_data')
        shutil.rmtree('archive')
        shutil.rmtree('custom_archive')
    def test_case_1(self):
        """Test archiving JSON files with the default archive directory."""
        success, errors = task_func('test_data')
        self.assertTrue(success)
        self.assertEqual(len(errors), 0)
        self.assertTrue(os.path.exists('archive/test1.json'))
        self.assertTrue(os.path.exists('archive/test2.json'))
    def test_case_2(self):
        """Test archiving with a custom archive directory."""
        success, errors = task_func('test_data', 'custom_archive')
        self.assertTrue(success)
        self.assertEqual(len(errors), 0)
        self.assertTrue(os.path.exists('custom_archive/test1.json'))
        self.assertTrue(os.path.exists('custom_archive/test2.json'))
    def test_case_3(self):
        """Test with a nonexistent source directory."""
        success, errors = task_func('nonexistent_directory')
        self.assertTrue(success)
        self.assertEqual(len(errors), 0)
    def test_case_4(self):
        """Test with an empty directory."""
        os.makedirs('empty_directory', exist_ok=True)
        success, errors = task_func('empty_directory')
        self.assertTrue(success)
        self.assertEqual(len(errors), 0)
        shutil.rmtree('empty_directory')
    def test_case_5(self):
        """Test that non-JSON files are not archived."""
        success, errors = task_func('test_data')
        self.assertTrue(success)
        self.assertEqual(len(errors), 0)
        self.assertFalse(os.path.exists('archive/test.txt'))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)