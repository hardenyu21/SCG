import os
import re

def task_func(pattern: str, replacement: str, directory: str) -> bool:
    try:
        # Compile the regex pattern for matching
        regex = re.compile(pattern)
        
        # Iterate over all files in the specified directory
        for filename in os.listdir(directory):
            # Check if the current file matches the pattern
            if regex.search(filename):
                # Create the new filename by replacing the pattern with the replacement string
                new_filename = regex.sub(replacement, filename)
                
                # Construct full file paths
                old_file_path = os.path.join(directory, filename)
                new_file_path = os.path.join(directory, new_filename)
                
                # Rename the file
                os.rename(old_file_path, new_file_path)
        
        # Return True if all operations were successful
        return True
    except Exception as e:
        # Return False if any exception occurred
        print(f"An error occurred: {e}")
        return False
import unittest
import tempfile
import shutil
from pathlib import Path
class TestCases(unittest.TestCase):
    
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        
    def tearDown(self):
        shutil.rmtree(self.test_dir)
    
    def create_test_files(self, filenames):
        for filename in filenames:
            Path(f"{self.test_dir}/{filename}").touch()
    
    def test_renafiles(self):
        self.create_test_files(["draft1.txt", "draft2.txt", "draft3.txt"])
        result = task_func("draft", "final", self.test_dir)
        self.assertTrue(result)
        expected_files = sorted(["final1.txt", "final2.txt", "final3.txt"])
        actual_files = sorted(os.listdir(self.test_dir))
        self.assertEqual(expected_files, actual_files)
        
    def test_no_matching_files(self):
        self.create_test_files(["file1.txt", "file2.txt", "file3.txt"])
        result = task_func("draft", "final", self.test_dir)
        self.assertTrue(result)
        expected_files = sorted(["file1.txt", "file2.txt", "file3.txt"])
        actual_files = sorted(os.listdir(self.test_dir))
        self.assertEqual(expected_files, actual_files)
        
    def test_nonexistent_directory(self):
        result = task_func("draft", "final", "/nonexistent/directory")
        self.assertFalse(result)
        
    def test_empty_directory(self):
        result = task_func("draft", "final", self.test_dir)
        self.assertTrue(result)
        self.assertEqual([], os.listdir(self.test_dir))
        
    def test_complex_pattern_renaming(self):
        self.create_test_files(["draft_file1.txt", "file_draft2.txt", "draft3file.txt"])
        result = task_func("draft", "final", self.test_dir)
        self.assertTrue(result)
        expected_files = sorted(["final_file1.txt", "file_final2.txt", "final3file.txt"])
        actual_files = sorted(os.listdir(self.test_dir))
        self.assertEqual(expected_files, actual_files)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)