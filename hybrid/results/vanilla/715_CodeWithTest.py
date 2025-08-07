import sys
import subprocess

# Constants
PYTHON_VERSION = '3.8'
PATH_TO_APPEND = '/path/to/whatever'

def task_func(python_version=PYTHON_VERSION, path_to_append=PATH_TO_APPEND):
    try:
        # Check if the specified Python version is installed
        result = subprocess.run(['python', '--version'], capture_output=True, text=True)
        current_version = result.stdout.strip().split()[1]
        
        if current_version != python_version:
            raise ValueError(f"Current Python version is {current_version}, but {python_version} is required.")
        
        # Append the specified path to sys.path if it's not already present
        if path_to_append not in sys.path:
            sys.path.append(path_to_append)
        
        return python_version
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    switched_version = task_func()
    if switched_version:
        print(f"Switched to Python version: {switched_version}")
    else:
        print("Failed to switch Python version.")
import sys
import unittest
from unittest.mock import patch
class TestCases(unittest.TestCase):
    @patch('subprocess.run')
    def test_switch_to_default_python_version(self, mock_run):
        original_path_length = len(sys.path)
        task_func()
        mock_run.assert_called_with(['pyenv', 'global', '3.8'], check=True)
        self.assertEqual(sys.path[-1], '/path/to/whatever')
        sys.path = sys.path[:original_path_length]  # Reset sys.path to original state
    @patch('subprocess.run')
    def test_switch_to_python_3_7(self, mock_run):
        original_path_length = len(sys.path)
        task_func('3.7', '/another/path')
        mock_run.assert_called_with(['pyenv', 'global', '3.7'], check=True)
        self.assertEqual(sys.path[-1], '/another/path')
        sys.path = sys.path[:original_path_length]
    @patch('subprocess.run')
    def test_switch_to_python_3_9(self, mock_run):
        original_path_length = len(sys.path)
        task_func('3.9')
        mock_run.assert_called_with(['pyenv', 'global', '3.9'], check=True)
        self.assertEqual(sys.path[-1], '/path/to/whatever')
        sys.path = sys.path[:original_path_length]
    @patch('subprocess.run')
    def test_switch_to_python_2_7(self, mock_run):
        original_path_length = len(sys.path)
        task_func('2.7')
        mock_run.assert_called_with(['pyenv', 'global', '2.7'], check=True)
        self.assertEqual(sys.path[-1], '/path/to/whatever')
        sys.path = sys.path[:original_path_length]
    @patch('subprocess.run')
    def test_switch_to_python_3_6(self, mock_run):
        original_path_length = len(sys.path)
        task_func('3.6', '/different/path')
        mock_run.assert_called_with(['pyenv', 'global', '3.6'], check=True)
        self.assertEqual(sys.path[-1], '/different/path')
        sys.path = sys.path[:original_path_length]


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)