import os
import hashlib

# Constants
DIRECTORY = "./hashed_files"

def task_func(input_string):
    # Ensure the directory exists
    if not os.path.exists(DIRECTORY):
        os.makedirs(DIRECTORY)
    
    # Split the input string into lines
    lines = input_string.splitlines()
    
    # List to store file paths
    file_paths = []
    
    # Iterate over each line
    for line in lines:
        # Ignore empty lines
        if not line.strip():
            continue
        
        # Compute the SHA256 hash of the line
        sha256_hash = hashlib.sha256(line.encode()).hexdigest()
        
        # Create the filename using the first 10 characters of the hash
        filename = f"{sha256_hash[:10]}.txt"
        file_path = os.path.join(DIRECTORY, filename)
        
        # Write the hash to the file
        with open(file_path, 'w') as file:
            file.write(sha256_hash)
        
        # Add the file path to the list
        file_paths.append(file_path)
    
    # Return the list of file paths
    return file_paths
import unittest
import os
import hashlib
import shutil
class TestCases(unittest.TestCase):
    """Tests for the function task_func."""
    def setUp(self):
        """Set up a temporary directory for test files."""
        self.temp_directory = "./temp_test_files"
        os.makedirs(self.temp_directory, exist_ok=True)
    def tearDown(self):
        """Clean up by removing the temporary directory after tests."""
        shutil.rmtree(self.temp_directory)
        dirs_to_remove = ["hashed_files"]
        for dir_path in dirs_to_remove:
            if os.path.exists(dir_path):
                shutil.rmtree(dir_path)
    def test_single_line(self):
        """Test with a single line input."""
        input_string = "Hello world"
        expected = [os.path.join("./hashed_files", "64ec88ca00.txt")]
        result = task_func(input_string)
        self.assertEqual(result, expected)
    def test_multi_line(self):
        """Test with a multi-line input."""
        input_string = "First line\nSecond line\nThird line"
        expected = [
            os.path.join("./hashed_files", "2361df1018.txt"),
            os.path.join("./hashed_files", "c8b588f708.txt"),
            os.path.join("./hashed_files", "3195807ae4.txt"),
        ]
        result = task_func(input_string)
        self.assertEqual(result, expected)
    def test_empty_input(self):
        """Test with an empty string."""
        input_string = ""
        expected = []
        result = task_func(input_string)
        self.assertEqual(result, expected)
    def test_input_with_empty_lines(self):
        """Test input string containing empty lines."""
        input_string = "Line one\n\nLine two\n"
        expected = [
            os.path.join("./hashed_files", "209f4c0be3.txt"),
            os.path.join("./hashed_files", "1ae5466eb8.txt"),
        ]
        result = task_func(input_string)
        self.assertEqual(result, expected)
    def test_no_newline_at_end(self):
        """Test input string without a newline at the end."""
        input_string = "Line with no newline at end"
        expected = [os.path.join("./hashed_files", "901dd863e9.txt")]
        result = task_func(input_string)
        self.assertEqual(result, expected)
    def test_directory_creation(self):
        """
        Test if the function creates the directory if it does not exist.
        """
        # Assert that the DIRECTORY does not exist before calling the function
        self.assertFalse(os.path.exists(DIRECTORY))
        # Call the function with any string
        task_func("Test for directory creation")
        # Check if the DIRECTORY has been created
        self.assertTrue(os.path.exists(DIRECTORY))
        # Optionally, clean up by removing the created directory after the test
        if os.path.exists(DIRECTORY):
            shutil.rmtree(DIRECTORY)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)