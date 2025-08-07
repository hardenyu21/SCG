import re
import os
import glob
import mimetypes

def task_func(directory, file_pattern, suffix):
    # Initialize an empty dictionary to store file names and their MIME types
    file_mime_dict = {}
    
    # Construct the search pattern using the provided file pattern and suffix
    search_pattern = os.path.join(directory, f"*{file_pattern}*{suffix}")
    
    # Use glob to find all files matching the pattern
    matching_files = glob.glob(search_pattern)
    
    # Iterate over each matching file
    for file_path in matching_files:
        # Extract the file name from the file path
        file_name = os.path.basename(file_path)
        
        # Determine the MIME type of the file
        mime_type, _ = mimetypes.guess_type(file_path)
        
        # If the MIME type is not None, add it to the dictionary
        if mime_type:
            file_mime_dict[file_name] = mime_type
    
    # Return the dictionary mapping file names to their MIME types
    return file_mime_dict
import unittest
from unittest.mock import patch, mock_open
import mimetypes
class TestCases(unittest.TestCase):
    def test_return_type(self):
        """Test that the function returns a dictionary."""
        with patch('os.chdir'), patch('glob.glob', return_value=[]), patch('re.search'):
            result = task_func('/path/to/directory', '*', '_suff')
        self.assertIsInstance(result, dict)
    @patch('glob.glob', return_value=['file_suff.txt', 'other_file.txt'])
    @patch('os.chdir')
    def test_dictionary_content(self, mock_chdir, mock_glob):
        """Test the content of the dictionary."""
        result = task_func('/path/to/directory', '*_suff.txt', '_suff')
        self.assertIn('file_suff.txt', result)
        self.assertNotIn('other_file.txt', result)
    @patch('mimetypes.guess_type', return_value=['text/plain'])
    @patch('glob.glob', return_value=['file_suff.txt'])
    @patch('os.chdir')
    def test_file_type_identification(self, mock_chdir, mock_glob, mock_guess_type):
        """Test correct file type identification."""
        result = task_func('/path/to/directory', '*', '_suff')
        self.assertEqual(result['file_suff.txt'], 'text/plain')
    @patch('glob.glob', return_value=[])
    @patch('os.chdir')
    def test_empty_directory(self, mock_chdir, mock_glob):
        """Test the function with an empty directory."""
        result = task_func('/path/to/directory', '*', '_suff')
        self.assertEqual(result, {})
    @patch('re.search', lambda pat, string: '_suff' in string)
    @patch('glob.glob', return_value=['test_suff', 'test', 'another_suff'])
    @patch('os.chdir')
    def test_re_search_called_with_suffix(self, mock_chdir, mock_glob):
        """Test that re.search is correctly used to filter files by suffix."""
        result = task_func('/path/to/directory', '*', '_suff')
        self.assertIn('test_suff', result)
        self.assertNotIn('test', result)
        self.assertIn('another_suff', result)
    @patch('re.search', return_value=False)
    @patch('glob.glob', return_value=['test_suff', 'test', 'another_suff'])
    @patch('os.chdir')
    def test_suffix_filtering(self, mock_chdir, mock_glob, mock_search):
        """Test that files not matching the suffix are correctly filtered out."""
        result = task_func('/path/to/directory', '*', '_suff')
        # Expecting an empty dictionary since mock_search is mocked to always return False, simulating no match
        self.assertEqual(result, {})


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)