import subprocess
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def task_func(filepath):
    try:
        # Check if the file exists
        with open(filepath, 'r'):
            pass
    except FileNotFoundError:
        logging.error(f"The specified file '{filepath}' does not exist.")
        raise FileNotFoundError(f"The specified file '{filepath}' does not exist.")

    # Define the compiler command
    compiler_command = ['g++', filepath, '-o', 'output_executable']

    try:
        # Run the compilation process
        subprocess.run(compiler_command, check=True)
        logging.info(f"Compilation of '{filepath}' was successful.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Compilation of '{filepath}' failed with error: {e}")
        raise subprocess.CalledProcessError(returncode=e.returncode, cmd=e.cmd, output=e.output, stderr=e.stderr)

# Example usage:
# task_func('example.cpp')
import os
import unittest
import logging
from unittest.mock import patch
class TestCases(unittest.TestCase):
    def setUp(self):
        # Setup an empty test file
        self.empty_file = './empty_file.cpp'
        with open(self.empty_file, 'w') as f:
            f.write("")
    @patch('subprocess.check_call')
    def test_successful_compilation(self, mock_check_call):
        task_func('example.cpp')
        mock_check_call.assert_called_with(['g++', 'example.cpp', '-o', 'example'])
    @patch('subprocess.check_call', side_effect=subprocess.CalledProcessError(1, ['g++']))
    def test_compilation_failure(self, mock_check_call):
        task_func('example.cpp')
        mock_check_call.assert_called_with(['g++', 'example.cpp', '-o', 'example'])
    
    @patch('logging.error')
    @patch('subprocess.check_call', side_effect=FileNotFoundError)
    def test_compiler_not_found(self, mock_check_call, mock_logging_error):
        task_func('example.cpp')
        mock_logging_error.assert_called()
    @patch('logging.error')
    def test_empty_file(self, mock_logging_error):
        task_func(self.empty_file)
        mock_logging_error.assert_called()
    @patch('logging.error')
    @patch('subprocess.check_call', side_effect=FileNotFoundError())
    def test_logging_output(self, mock_check_call, mock_logging):
        task_func('example.cpp')
        mock_logging.assert_called()
    def tearDown(self):
        # Clean up created files
        os.remove(self.empty_file)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)