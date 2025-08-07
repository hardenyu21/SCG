import os
from pathlib import Path
from datetime import datetime, timezone

def task_func(directory_path: str):
    # Check if the directory exists
    if not os.path.exists(directory_path):
        raise ValueError("The provided directory does not exist.")
    
    # Ensure the provided path is a directory
    if not os.path.isdir(directory_path):
        raise ValueError("The provided path is not a directory.")
    
    # Initialize an empty list to store the results
    result = []
    
    # Iterate over each entry in the directory
    for entry in os.scandir(directory_path):
        # Check if the entry is a file
        if entry.is_file():
            # Get the file name
            file_name = entry.name
            
            # Get the file size
            file_size = entry.stat().st_size
            
            # Get the creation time, if available, otherwise use the last metadata change time
            try:
                creation_time = datetime.fromtimestamp(entry.stat().st_ctime, tz=timezone.utc).isoformat()
            except AttributeError:
                creation_time = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
            
            # Get the last modification time
            modification_time = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
            
            # Append the tuple to the result list
            result.append((file_name, file_size, creation_time, modification_time))
    
    return result
import unittest
import tempfile
import os
from datetime import datetime, timezone, timedelta
class TestCases(unittest.TestCase):
    def setUp(self):
        # Set up a 'before' time with leeway for testing file modification times
        self.before_creation = datetime.now(timezone.utc) - timedelta(seconds=1)
        # Setup a temporary directory
        self.test_dir = tempfile.TemporaryDirectory()
        # Create test files
        self.files = {
            "empty.txt": 0,
            "small.txt": 5,
            "medium.txt": 50,
            "large.txt": 500,
            "utc_test.txt": 10,
        }
        for file_name, size in self.files.items():
            path = os.path.join(self.test_dir.name, file_name)
            with open(path, "wb") as f:
                f.write(os.urandom(size))
    def tearDown(self):
        # Cleanup the directory after tests
        self.test_dir.cleanup()
    def test_case_1(self):
        # Test the function on an existing directory.
        result = task_func(self.test_dir.name)
        self.assertEqual(len(result), len(self.files))
    def test_case_2(self):
        # Test the function with a non-existing directory.
        with self.assertRaises(ValueError):
            task_func("/path/to/non/existing/directory")
    def test_case_3(self):
        # Test the function with an empty directory.
        with tempfile.TemporaryDirectory() as empty_dir:
            result = task_func(empty_dir)
            self.assertEqual(len(result), 0)
    def test_case_4(self):
        # Test if the function correctly identifies file sizes.
        result = task_func(self.test_dir.name)
        sizes = {file[0]: file[1] for file in result}
        for file_name, size in self.files.items():
            self.assertEqual(sizes[file_name], size)
    def test_case_5(self):
        # Test if the function lists all expected files, regardless of order.
        result = task_func(self.test_dir.name)
        file_names = sorted([file[0] for file in result])
        expected_file_names = sorted(
            list(self.files.keys())
        )  # Assuming 'utc_test.txt' is expected.
        self.assertListEqual(file_names, expected_file_names)
    def test_case_6(self):
        # Test if modification times are correctly identified.
        result = task_func(self.test_dir.name)
        # Check if modification times are reasonable (not testing specific times because of system differences)
        for _, _, creation_time, modification_time in result:
            creation_datetime = datetime.fromisoformat(creation_time)
            modification_datetime = datetime.fromisoformat(modification_time)
            self.assertTrue(creation_datetime <= modification_datetime)
    def test_case_7(self):
        # Test that the function ignores directories.
        sub_dir_path = os.path.join(self.test_dir.name, "subdir")
        os.mkdir(sub_dir_path)
        # Add a file inside the sub-directory to ensure it's not empty
        with open(os.path.join(sub_dir_path, "file.txt"), "w") as sub_file:
            sub_file.write("This is a test.")
        result = task_func(self.test_dir.name)
        self.assertEqual(
            len(result), len(self.files)
        )  # Should not count the subdir or its contents
    def test_case_8(self):
        # Test if file names are correctly identified.
        result = task_func(self.test_dir.name)
        names = [file[0] for file in result]
        for name in self.files.keys():
            self.assertIn(name, names)
    def test_case_9(self):
        # Test that a non-directory path raises a ValueError.
        with tempfile.NamedTemporaryFile() as tmpfile:
            with self.assertRaises(ValueError):
                task_func(tmpfile.name)
    def test_case_10(self):
        # Test timestamps are in UTC and within a reasonable accuracy window.
        self.after_creation = datetime.now(timezone.utc)
        result = task_func(self.test_dir.name)
        for _, _, creation_time, modification_time in result:
            creation_dt = datetime.fromisoformat(creation_time)
            modification_dt = datetime.fromisoformat(modification_time)
            # Ensure the timestamps are in UTC
            self.assertEqual(creation_dt.tzinfo, timezone.utc)
            self.assertEqual(modification_dt.tzinfo, timezone.utc)
            # Ensure timestamps are within a reasonable window
            self.assertTrue(self.before_creation <= creation_dt <= self.after_creation)
            self.assertTrue(
                self.before_creation <= modification_dt <= self.after_creation
            )


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)