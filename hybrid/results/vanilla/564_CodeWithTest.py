import os
import ctypes
from datetime import datetime
import pytz

def task_func(filepath):
    # Load the DLL file using ctypes
    try:
        dll = ctypes.CDLL(filepath)
    except OSError as e:
        return f"Error loading DLL: {e}", {}

    # Get the DLL file name
    dll_name = os.path.basename(filepath)

    # Get file metadata
    try:
        # Get creation time
        creation_time = os.path.getctime(filepath)
        creation_time_utc = datetime.fromtimestamp(creation_time, pytz.utc)

        # Get modification time
        modification_time = os.path.getmtime(filepath)
        modification_time_utc = datetime.fromtimestamp(modification_time, pytz.utc)

        # Get file size
        file_size = os.path.getsize(filepath)

        # Prepare metadata dictionary
        metadata = {
            'Creation Time': creation_time_utc.isoformat(),
            'Modification Time': modification_time_utc.isoformat(),
            'Size': file_size
        }

        return dll_name, metadata

    except OSError as e:
        return f"Error accessing file metadata: {e}", {}

# Example usage:
# dll_name, metadata = task_func('path_to_your_dll.dll')
# print(f"Loaded DLL: {dll_name}")
# print("Metadata:", metadata)
import unittest
import os
import ctypes
from unittest.mock import patch
import tempfile
import sys
from datetime import datetime
import pytz
from io import StringIO
class TestCases(unittest.TestCase):
    def setUp(self):
        # Create a temporary DLL file
        self.temp_file = tempfile.NamedTemporaryFile(suffix='.dll', delete=False)
        self.filepath = self.temp_file.name
    def test_file_existence(self):
        self.assertTrue(os.path.exists(self.filepath))
    def test_invalid_file_path(self):
        with self.assertRaises(OSError):
            task_func('invalid_path.dll')
    @patch('ctypes.CDLL')
    @patch('os.stat')
    def test_return_value(self, mock_stat, mock_cdll):
        """Verify that the function returns the name of the DLL file."""
        mock_cdll.return_value._name = 'test.dll'
        result, metadata = task_func('path/to/test.dll')
        self.assertEqual(result, 'test.dll')
        self.assertIsInstance(metadata, dict)
    @patch('ctypes.CDLL', side_effect=OSError("File not found"))
    def test_nonexistent_file(self, mock_cdll):
        """Ensure function handles nonexistent files appropriately."""
        with self.assertRaises(OSError) as context:
            task_func('path/to/nonexistent.dll')
        self.assertEqual(str(context.exception), "File not found")
    @patch('os.stat')
    @patch('ctypes.CDLL')
    def test_metadata_printing(self, mock_cdll, mock_stat):
        """Check if file metadata is correctly printed."""
        # Setup mock for os.stat to return specific file metadata
        mock_stat.return_value.st_ctime = 1609459200  # 2021-01-01 00:00:00 UTC
        mock_stat.return_value.st_mtime = 1609545600  # 2021-01-02 00:00:00 UTC
        mock_stat.return_value.st_size = 123456
        # Setup mock for CDLL to return a dummy name
        mock_cdll.return_value._name = 'test.dll'
        # Set the expected output dictionary
        expected_output = {
            'Creation Time': datetime(2021, 1, 1, 0, 0, 0, tzinfo=pytz.UTC),
            'Modification Time': datetime(2021, 1, 2, 0, 0, 0, tzinfo=pytz.UTC),
            'Size': 123456
        }
        # Call the function
        result, metadata = task_func('path/to/test.dll')
        # Check if the output matches the expected dictionary
        self.assertEqual(result, 'test.dll', expected_output)
        self.assertEqual(metadata, expected_output)
        
    def tearDown(self):
        os.remove(self.filepath)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)