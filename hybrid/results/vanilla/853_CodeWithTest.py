import os
import shutil
import string

# Constants
INVALID_CHARACTERS = string.punctuation + string.whitespace

def task_func(directory_path):
    # Initialize summary dictionary
    summary = {}

    # Create the "Invalid" directory if it doesn't exist
    invalid_dir = os.path.join(directory_path, "Invalid")
    if not os.path.exists(invalid_dir):
        os.makedirs(invalid_dir)
        summary["Invalid"] = 0

    # Iterate over all files in the given directory
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Check for invalid characters in the filename
        if any(char in INVALID_CHARACTERS for char in filename):
            # Move invalid files to the "Invalid" directory
            shutil.move(file_path, os.path.join(invalid_dir, filename))
            summary["Invalid"] += 1
            continue

        # Determine the file extension
        _, file_extension = os.path.splitext(filename)

        # Create a directory for the file extension if it doesn't exist
        extension_dir = os.path.join(directory_path, file_extension)
        if not os.path.exists(extension_dir):
            os.makedirs(extension_dir)
            summary[file_extension] = 0

        # Move the file to the corresponding extension directory
        shutil.move(file_path, os.path.join(extension_dir, filename))
        summary[file_extension] += 1

    return summary

# Example usage:
# summary = task_func('/path/to/directory')
# print(summary)
import unittest
import os
import shutil
import tempfile
class TestCases(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.test_dir_1 = os.path.join(self.temp_dir, 'test_dir_1')
        self.empty_dir = os.path.join(self.temp_dir, 'empty_dir')
        os.mkdir(self.test_dir_1)
        os.mkdir(self.empty_dir)
        self.create_test_files(self.test_dir_1, ['test1.pdf', 'data.csv', 'image.jpg', 'invalid file name.jpg'])
    def tearDown(self):
        shutil.rmtree(self.temp_dir)
    def create_test_files(self, directory, filenames):
        for filename in filenames:
            path = os.path.join(directory, filename)
            with open(path, 'w') as f:
                f.write("Dummy content")
    def test_file_moves(self):
        task_func(self.test_dir_1)
        invalid_dir = os.path.join(self.test_dir_1, 'Invalid')
        self.assertTrue(os.path.exists(invalid_dir))
        self.assertEqual(len(os.listdir(invalid_dir)), 4)
    def test_empty_directory(self):
        summary = task_func(self.empty_dir)
        self.assertEqual(summary, {})
    def test_basic_functionality(self):
        # Test basic functionality
        summary = task_func(self.test_dir_1)
        expected = {'Invalid': 4}
        self.assertEqual(summary, expected)
        
    def test_invalid_path(self):
        # Test with an invalid directory path
        with self.assertRaises(FileNotFoundError):
            task_func('invalid_path')
    def test_summary_content(self):
        # Test the summary content details
        summary = task_func(self.test_dir_1)
        
        # Check if the summary contains keys for all unique extensions and "Invalid"
        self.assertTrue(all(key in ['pdf', 'csv', 'jpg', 'Invalid'] for key in summary.keys()))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)