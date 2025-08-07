import sys
from pathlib import Path

# Constants
PATH_TO_APPEND = '/path/to/whatever'

def task_func(path_to_append=PATH_TO_APPEND):
    # Append the path to sys.path if it's not already there
    if path_to_append not in sys.path:
        sys.path.append(path_to_append)
    
    # Create a Path object for the directory
    directory_path = Path(path_to_append)
    
    # Create the directory if it does not exist
    if not directory_path.exists():
        directory_path.mkdir(parents=True, exist_ok=True)
    
    # Output the path that was appended and where the directory was created
    return path_to_append

# Example usage
print(task_func())
import tempfile
import unittest
class TestCases(unittest.TestCase):
    def setUp(self):
        # Creating a temporary directory
        self.temp_dir = tempfile.TemporaryDirectory()
        # Removing the appended path from sys.path for each test case
        if self.temp_dir.name + '/test/path' in sys.path:
            sys.path.remove(self.temp_dir.name + '/test/path')
        if self.temp_dir.name + '/another/test/path' in sys.path:
            sys.path.remove(self.temp_dir.name + '/another/test/path')
    def tearDown(self):
        # Cleaning up the temporary directory
        self.temp_dir.cleanup()
    def test_1(self):
        # Testing with the default path
        result = task_func(self.temp_dir.name + '/path/to/whatever')
        self.assertEqual(result, self.temp_dir.name + '/path/to/whatever')
        self.assertTrue(self.temp_dir.name + '/path/to/whatever' in sys.path)
        self.assertTrue(Path(self.temp_dir.name + '/path/to/whatever').exists())
    def test_2(self):
        # Testing with a custom path
        result = task_func(self.temp_dir.name + '/test/path')
        self.assertEqual(result, self.temp_dir.name + '/test/path')
        self.assertTrue(self.temp_dir.name + '/test/path' in sys.path)
        self.assertTrue(Path(self.temp_dir.name + '/test/path').exists())
    def test_3(self):
        # Testing if the directory is actually created
        task_func(self.temp_dir.name + '/another/test/path')
        self.assertTrue(Path(self.temp_dir.name + '/another/test/path').exists())
    def test_4(self):
        # Testing if the path is appended to sys.path
        task_func(self.temp_dir.name + '/test/path')
        self.assertTrue(self.temp_dir.name + '/test/path' in sys.path)
    def test_5(self):
        # Testing if the function returns the correct path
        result = task_func(self.temp_dir.name + '/test/path')
        self.assertEqual(result, self.temp_dir.name + '/test/path')


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)