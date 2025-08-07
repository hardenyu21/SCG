import subprocess
import os
import random

def task_func(directory, file_list):
    if not file_list:
        return None

    # Select a random file from the list
    random_file = random.choice(file_list)

    # Construct the full path to the file
    file_path = os.path.join(directory, random_file)

    # Check if the file exists and is executable
    if not os.path.isfile(file_path) or not os.access(file_path, os.X_OK):
        return None

    # Run the file as a subprocess
    try:
        result = subprocess.run(file_path, check=False)
        return result.returncode
    except Exception as e:
        print(f"An error occurred while running the file: {e}")
        return None
import unittest
import subprocess
from unittest.mock import patch, MagicMock
import random
class TestCases(unittest.TestCase):
    def test_valid_input(self):
        random.seed(0)
        # Testing with a valid directory and file list
        directory = "valid_dir"
        file_list = ["script1.bat", "script2.bat"]
        with patch('subprocess.Popen') as mock_popen:
            mock_process = MagicMock()
            mock_process.wait.return_value = None
            mock_process.returncode = 0
            mock_popen.return_value = mock_process
            result = task_func(directory, file_list)
            self.assertEqual(result, 0)
    def test_empty_file_list(self):
        # Testing with an empty file list
        random.seed(0)
        directory = "valid_dir"
        file_list = []
        result = task_func(directory, file_list)
        self.assertIsNone(result)
    def test_invalid_directory(self):
        # Testing with an invalid directory
        random.seed(0)
        directory = "invalid_dir"
        file_list = ["script1.bat"]
        with patch('subprocess.Popen', side_effect=Exception("Error")):
            result = task_func(directory, file_list)
            self.assertIsNone(result)
    def test_non_zero_exit_code(self):
        # Testing a subprocess that returns a non-zero exit code
        random.seed(0)
        directory = "valid_dir"
        file_list = ["script3.bat"]
        with patch('subprocess.Popen') as mock_popen:
            mock_process = MagicMock()
            mock_process.wait.return_value = None
            mock_process.returncode = 1
            mock_popen.return_value = mock_process
            result = task_func(directory, file_list)
            self.assertEqual(result, 1)
    def test_random_file_selection(self):
        # Testing that a file is randomly selected from the list
        random.seed(0)
        directory = "valid_dir"
        file_list = ["script1.bat", "script2.bat", "script3.bat"]
        with patch('random.choice', side_effect=file_list):
            with patch('subprocess.Popen') as mock_popen:
                mock_process = MagicMock()
                mock_process.wait.return_value = None
                mock_process.returncode = 0
                mock_popen.return_value = mock_process
                for expected_file in file_list:
                    result = task_func(directory, file_list)
                    # Manually check that the expected command was part of any call
                    expected_call = os.path.join(directory, expected_file)
                    found = False
                    for call in mock_popen.call_args_list:
                        call_args, call_kwargs = call
                        if call_args[0] == expected_call:
                            found = True
                            break
                    self.assertTrue(found, f"Expected call with {expected_call} not found")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)