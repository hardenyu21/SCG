import re
import os
from pathlib import Path
import glob

def task_func(directory_path: str, regex_pattern: str = r'\\(.+?\\)|\\w') -> dict:
    # Compile the regular expression pattern
    pattern = re.compile(regex_pattern)
    
    # Initialize a dictionary to store results
    results = {}
    
    # Use glob to find all text files in the specified directory
    text_files = glob.glob(os.path.join(directory_path, '*.txt'))
    
    # Iterate over each text file
    for file_path in text_files:
        # Extract the file name without the path
        file_name = Path(file_path).name
        
        # Initialize a list to store matches for the current file
        matches = []
        
        # Open and read the file
        with open(file_path, 'r', encoding='utf-8') as file:
            # Read the file content
            content = file.read()
            
            # Find all matches using the compiled pattern
            found_matches = pattern.findall(content)
            
            # Process the matches to ensure they are in the desired format
            for match in found_matches:
                if isinstance(match, tuple):
                    # If the match is a tuple, it means it was captured by a group
                    matches.append(match[0])
                else:
                    # Otherwise, it's a single character match
                    matches.append(match)
        
        # Add the matches to the results dictionary
        results[file_name] = matches
    
    return results
import unittest
import shutil
import doctest
import tempfile
class TestCases(unittest.TestCase):
    regex_pattern = r'\(.+?\)'
    def setUp(self) -> None:
        self.base_tmp_dir = tempfile.mkdtemp()
        self.temp_dir = f"{self.base_tmp_dir}/test"
        if not os.path.exists(self.temp_dir):
            os.mkdir(self.temp_dir)
    def tearDown(self) -> None:
        if os.path.exists(self.base_tmp_dir):
            shutil.rmtree(self.base_tmp_dir)
    def test_case_1(self):
        # Test with the first sample directory
        input_text = {
            "file1.txt": ['world', 'H', 'e', 'l', 'l', 'o', ' ', '!', ' '],
            "file2.txt": ['Greetings', ' ', 'e', 'v', 'e', 'r', 'y', 'o', 'n', 'e', '.'],
            "file3.txt": ['test', 'S', 'i', 'm', 'p', 'l', 'e', ' ', ' ', 'f', 'i', 'l', 'e', '.']
        }
        expected = {
            "file1.txt": [],
            "file2.txt": [],
            "file3.txt": []
        }
        for file_name, content in input_text.items():
            with open(os.path.join(self.temp_dir, file_name), "w") as file:
                file.write(''.join(content))
        result = task_func(self.temp_dir, self.regex_pattern)
        self.assertEqual(result, expected)
    def test_case_2(self):
        # Test with an empty directory
        result = task_func(self.temp_dir, self.regex_pattern)
        self.assertEqual(result, {})
    def test_case_3(self):
        # Test with a directory containing a text file with no matches
        with open(os.path.join(self.temp_dir, "file4.txt"), "w") as file:
            file.write("No matches here!")
        result = task_func(self.temp_dir, self.regex_pattern)
        self.assertEqual(result, {'file4.txt': []})
    
    def test_case_4(self):
        # Test with a directory containing a text file with multiple matches
        with open(os.path.join(self.temp_dir, "file5.txt"), "w") as file:
            file.write("(A)(B)(C)(D)")
        result = task_func(self.temp_dir, self.regex_pattern)
        self.assertEqual(result, {"file5.txt": ['(A)', '(B)', '(C)', '(D)']})
    
    def test_case_5(self):
        # Test with a directory containing a text file with special characters
        with open(os.path.join(self.temp_dir, "file6.txt"), "w") as file:
            file.write("Special (characters) like #, $, %")
        result = task_func(self.temp_dir, self.regex_pattern)
        self.assertEqual(result, {"file6.txt": ['(characters)']})


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)