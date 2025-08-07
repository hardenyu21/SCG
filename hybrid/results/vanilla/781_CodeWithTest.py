import os
from datetime import datetime

def task_func(filepath: str) -> dict:
    try:
        # Get the size of the file in bytes
        size = os.path.getsize(filepath)
        
        # Get the last modification time of the file
        mod_time = os.path.getmtime(filepath)
        
        # Convert the modification time to a readable format
        mod_date = datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d %H:%M:%S')
        
        # Return the results in a dictionary
        return {
            'size': size,
            'last_modified': mod_date
        }
    except FileNotFoundError:
        return {'error': 'File not found'}
    except Exception as e:
        return {'error': str(e)}
import unittest
import os
from datetime import datetime
from unittest.mock import patch
import errno
def create_test_files(base_path):
    os.makedirs(base_path, exist_ok=True)
    with open(os.path.join(base_path, "empty_file.txt"), 'w') as f:
        pass
    with open(os.path.join(base_path, "large_file.txt"), 'w') as f:
        f.write("A" * 10**6)  # 1MB file
class TestCases(unittest.TestCase):
    def setUp(self):
        self.base_path = "task_func_data"
        create_test_files(self.base_path)
    def tearDown(self):
        for item in os.listdir(self.base_path):
            os.remove(os.path.join(self.base_path, item))
        os.rmdir(self.base_path)
    def test_file_properties(self):
        file_path = os.path.join(self.base_path, "large_file.txt")
        result = task_func(file_path)
        expected_size = os.path.getsize(file_path)
        expected_mtime = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d %H:%M:%S')
        self.assertEqual(result['size'], f"{expected_size} bytes")
        self.assertEqual(result['last_modified'], expected_mtime)
    def test_empty_file(self):
        file_path = os.path.join(self.base_path, "empty_file.txt")
        result = task_func(file_path)
        self.assertEqual(result['size'], "0 bytes")
    def test_file_not_found(self):
        file_path = os.path.join(self.base_path, "nonexistent.txt")
        with self.assertRaises(Exception) as context:
            task_func(file_path)
        self.assertIn("No such file or directory", str(context.exception))
    @patch('os.path.getsize')
    @patch('os.path.getmtime')
    def test_permission_error(self, mock_getmtime, mock_getsize):
        mock_getsize.side_effect = OSError(errno.EACCES, "Permission denied")
        mock_getmtime.side_effect = OSError(errno.EACCES, "Permission denied")
        
        with self.assertRaises(Exception) as context:
            task_func("fakepath/file.txt")
        self.assertIn("Permission denied", str(context.exception))
    def test_large_file(self):
        file_path = os.path.join(self.base_path, "large_file.txt")
        result = task_func(file_path)
        self.assertTrue(int(result['size'].replace(' bytes', '')) > 0)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)