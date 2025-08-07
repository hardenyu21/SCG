import re
import os
import glob

def task_func(dir_path: str) -> list:
    # Compile a regular expression pattern to match all non-alphanumeric characters
    pattern = re.compile(r'[^a-zA-Z0-9]')
    
    # List to store the new file names
    new_file_names = []
    
    # Get all files in the specified directory
    for file_path in glob.glob(os.path.join(dir_path, '*')):
        # Extract the file name from the file path
        file_name = os.path.basename(file_path)
        
        # Remove all non-alphanumeric characters from the file name
        new_file_name = pattern.sub('', file_name)
        
        # Construct the new file path
        new_file_path = os.path.join(dir_path, new_file_name)
        
        # Rename the file if the new file name is different from the old one
        if new_file_name != file_name:
            os.rename(file_path, new_file_path)
        
        # Add the new file name to the list
        new_file_names.append(new_file_name)
    
    return new_file_names
import unittest
from pathlib import Path
import shutil
class TestCases(unittest.TestCase):
    
    def setUp(self):
        self.temp_dir = Path("temp_test_dir")
        self.temp_dir.mkdir(parents=True, exist_ok=True)
    
    def tearDown(self):
        shutil.rmtree(self.temp_dir)
    
    def test_special_characters_removal(self):
        test_files = ["file@1.txt", "file_#2.txt", "file$ 3.txt"]
        for file_name in test_files:
            (self.temp_dir / file_name).touch()
        
        expected_names = ["file1txt", "file2txt", "file3txt"]
        new_file_names = task_func(str(self.temp_dir))
        
        self.assertListEqual(sorted(new_file_names), sorted(expected_names))
    
    def test_alphanumeric_names(self):
        test_files = ["file1.txt", "file2.txt", "file3.txt"]
        for file_name in test_files:
            (self.temp_dir / file_name).touch()
        
        expected_names = ["file1txt", "file2txt", "file3txt"]
        new_file_names = task_func(str(self.temp_dir))
        
        self.assertListEqual(sorted(new_file_names), sorted(expected_names))
    
    def test_empty_directory(self):
        expected_names = []
        new_file_names = task_func(str(self.temp_dir))
        
        self.assertListEqual(new_file_names, expected_names)
    
    def test_only_special_characters(self):
        test_files = ["@@@.txt", "###.txt", "$$$ .txt"]
        for file_name in test_files:
            (self.temp_dir / file_name).touch()
        
        expected_names = ["txt", "txt", "txt"]
        new_file_names = task_func(str(self.temp_dir))
        
        self.assertListEqual(sorted(new_file_names), sorted(expected_names))
    
    def test_mixed_characters(self):
        test_files = ["f@ile_1.txt", "file# 2.txt", "fi$le 3.txt"]
        for file_name in test_files:
            (self.temp_dir / file_name).touch()
        
        expected_names = ["file1txt", "file2txt", "file3txt"]
        new_file_names = task_func(str(self.temp_dir))
        
        self.assertListEqual(sorted(new_file_names), sorted(expected_names))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)