import re
import os
import glob

def task_func(dir_path):
    # Check if the directory exists
    if not os.path.exists(dir_path):
        raise ValueError(f"The directory '{dir_path}' does not exist.")
    
    # Dictionary to store the count of "error" occurrences
    error_count = {}
    
    # Use glob to find all .txt files in the directory and its subdirectories
    txt_files = glob.glob(os.path.join(dir_path, '**', '*.txt'), recursive=True)
    
    # Regular expression to find occurrences of "error" (case insensitive)
    error_pattern = re.compile(r'\berror\b', re.IGNORECASE)
    
    # Iterate over each text file
    for file_path in txt_files:
        # Calculate the relative file path
        relative_path = os.path.relpath(file_path, dir_path)
        
        # Initialize the count for this file
        count = 0
        
        # Open and read the file
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # Find all occurrences of "error" in the line
                matches = error_pattern.findall(line)
                # Increment the count by the number of matches
                count += len(matches)
        
        # Store the count in the dictionary
        error_count[relative_path] = count
    
    return error_count
import unittest
import os
import shutil
import tempfile
class TestCases(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory to simulate test environments
        self.test_dir = tempfile.mkdtemp()
    def tearDown(self):
        # Remove the temporary directory after the test
        shutil.rmtree(self.test_dir)
    def create_file(self, sub_path, content=""):
        # Helper method to create a file with given content
        full_path = os.path.join(self.test_dir, sub_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, 'w') as file:
            file.write(content)
        # Return normalized path for cross-platform compatibility
        return os.path.normpath(sub_path)
    def test_non_existent(self):
        # Expect ValueError for non-existent directory
        with self.assertRaises(ValueError):
            task_func(os.path.join(self.test_dir, "non_existent"))
    def test_empty_folder(self):
        # Test empty directory
        result = task_func(self.test_dir)
        self.assertEqual(result, {})
    def test_files_with_errors(self):
        # Files with varying counts of 'error'
        files = {
            "1.txt": "error\nERROR\nErrOr",
            "subfolder1/2.txt": "",
            "subfolder2/3.txt": "error\nerror error"
        }
        expected = {
            os.path.normpath("1.txt"): 3,
            os.path.normpath("subfolder1/2.txt"): 0,
            os.path.normpath("subfolder2/3.txt"): 3
        }
        for path, content in files.items():
            self.create_file(path, content)
        result = task_func(self.test_dir)
        self.assertEqual(result, expected)
    def test_case_sensitive_and_realistic_text(self):
        # More complex scenarios, including nested directories
        file_path = self.create_file('nested/folder1/folder2/error_log.txt', 'Error\nerror\nERROR')
        expected = {file_path: 3}
        result = task_func(self.test_dir)
        self.assertEqual(result, expected)
    def test_exact_word_matching(self):
        # Ensure only the exact word 'error' is counted and ignore similar words like 'errors'
        files = {
            "file1.txt": "error error error",  # Should count 3 times
            "subdir/file2.txt": "errors error erro errors",  # Should count 1 time
            "subdir2/nested/file3.txt": "an error occurred",  # Should count 1 time
            "subdir3/file4.txt": "no errors here",  # Should count 0 times
            "subdir3/file5.txt": "Error and ERROR and error"  # Should count 3 times, case insensitive
        }
        expected = {
            os.path.normpath("file1.txt"): 3,
            os.path.normpath("subdir/file2.txt"): 1,
            os.path.normpath("subdir2/nested/file3.txt"): 1,
            os.path.normpath("subdir3/file4.txt"): 0,
            os.path.normpath("subdir3/file5.txt"): 3
        }
        for path, content in files.items():
            self.create_file(path, content)
        result = task_func(self.test_dir)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)