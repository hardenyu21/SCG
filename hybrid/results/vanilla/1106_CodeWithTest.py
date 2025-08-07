from datetime import datetime
import os
from pathlib import Path

# Constants
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

def task_func(file_path):
    # Convert the file path to a Path object
    path = Path(file_path)
    
    # Check if the file exists
    if not path.exists():
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    # Get the creation time of the file
    creation_time = path.stat().st_ctime
    
    # Convert the creation time to a datetime object
    creation_datetime = datetime.fromtimestamp(creation_time)
    
    # Format the datetime object to the desired string format
    formatted_time = creation_datetime.strftime(DATE_FORMAT)
    
    return formatted_time
import unittest
from datetime import datetime
import os
from pathlib import Path
import shutil
def create_dummy_file(filename):
    """Creates a dummy file and returns its creation time."""
    with open(filename, 'w') as f:
        f.write("This is a dummy file.")
    return os.path.getctime(filename)
class TestCases(unittest.TestCase):
    
    def setUp(self):
        """Setup function to create dummy files for testing."""
        self.file1 = "dummy_f954_1.txt"
        self.file2 = "dummy_f954_2.txt"
        self.file3 = "dummy_f954_3.txt"
        self.creation_time1 = create_dummy_file(self.file1)
        self.creation_time2 = create_dummy_file(self.file2)
        self.creation_time3 = create_dummy_file(self.file3)
        self.test_dir = 'testdir_task_func/'
        os.makedirs(self.test_dir, exist_ok=True)
    
    def tearDown(self):
        """Cleanup function to remove dummy files after testing."""
        os.remove(self.file1)
        os.remove(self.file2)
        os.remove(self.file3)
        shutil.rmtree(self.test_dir)
    def test_case_1(self):
        expected_output = datetime.fromtimestamp(self.creation_time1).strftime('%Y-%m-%d %H:%M:%S')
        self.assertEqual(task_func(self.file1), expected_output)
        
    def test_case_2(self):
        expected_output = datetime.fromtimestamp(self.creation_time2).strftime('%Y-%m-%d %H:%M:%S')
        self.assertEqual(task_func(self.file2), expected_output)
        
    def test_case_3(self):
        expected_output = datetime.fromtimestamp(self.creation_time3).strftime('%Y-%m-%d %H:%M:%S')
        self.assertEqual(task_func(self.file3), expected_output)
        
    def test_case_4(self):
        # Test for non-existing file
        with self.assertRaises(FileNotFoundError):
            task_func("non_existing_file.txt")
    
    def test_case_5(self):
        # Test for a directory
        dir_creation_time = os.path.getctime(self.test_dir)
        expected_output = datetime.fromtimestamp(dir_creation_time).strftime('%Y-%m-%d %H:%M:%S')
        self.assertEqual(task_func(self.test_dir), expected_output)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)