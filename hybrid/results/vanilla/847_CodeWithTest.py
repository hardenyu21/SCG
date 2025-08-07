import re
import os
import string
import random

def task_func(input_string, directory='./text_files'):
    # Ensure the directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Split the input string into separate lines
    lines = input_string.splitlines()
    
    # Prepare a list to store file paths
    file_paths = []
    
    # Iterate over each line
    for i, line in enumerate(lines):
        # Remove special characters using regex
        cleaned_line = re.sub(f'[{re.escape(string.punctuation)}]', '', line)
        
        # Generate a random filename to avoid conflicts
        random_suffix = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        filename = f"file_{i+1}_{random_suffix}.txt"
        file_path = os.path.join(directory, filename)
        
        # Write the cleaned line to a file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(cleaned_line)
        
        # Add the file path to the list
        file_paths.append(file_path)
    
    return file_paths
import unittest
import os
import random
import string
# Importing the refined function
class TestCases(unittest.TestCase):
    def setUp(self):
        # Set up the directory where test files will be saved
        self.test_dir = './test_text_files'
        os.makedirs(self.test_dir, exist_ok=True)
    def tearDown(self):
        # Remove all files in the test directory after each test
        for file_name in os.listdir(self.test_dir):
            file_path = os.path.join(self.test_dir, file_name)
            os.remove(file_path)
    def test_single_line(self):
        # Test with a single line string
        input_string = "Hello, world!"
        output = task_func(input_string, self.test_dir)
        self.assertEqual(len(output), 1)
        with open(output[0], 'r') as file:
            self.assertEqual(file.read(), "Hello world")
    def test_multi_line(self):
        # Test with a multi-line string
        input_string = "Line A\nLine B\nLine C"
        output = task_func(input_string, self.test_dir)
        self.assertEqual(len(output), 3)
        expected_lines = ["Line A", "Line B", "Line C"]
        for i, file_path in enumerate(output):
            with open(file_path, 'r') as file:
                self.assertEqual(file.read(), expected_lines[i])
    def test_special_characters(self):
        # Test if special characters are removed
        input_string = "Hello!@$\nWorld!#"
        output = task_func(input_string, self.test_dir)
        self.assertEqual(len(output), 2)
        expected_lines = ["Hello", "World"]
        for i, file_path in enumerate(output):
            with open(file_path, 'r') as file:
                self.assertEqual(file.read(), expected_lines[i])
    def test_empty_string(self):
        # Test with an empty string
        input_string = ""
        output = task_func(input_string, self.test_dir)
        self.assertEqual(len(output), 1)
        with open(output[0], 'r') as file:
            self.assertEqual(file.read(), "")
    def test_random_filenames(self):
        # Test if filenames are random and unique
        input_string = "A\nB"
        output1 = task_func(input_string, self.test_dir)
        output2 = task_func(input_string, self.test_dir)
        self.assertNotEqual(output1, output2)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)