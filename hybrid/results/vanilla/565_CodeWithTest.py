import ctypes
import hashlib
import binascii

def task_func(filepath):
    # Load the DLL file
    try:
        dll = ctypes.CDLL(filepath)
    except OSError as e:
        print(f"Error loading DLL: {e}")
        return None

    # Get the actual name of the loaded DLL file
    dll_name = dll._name

    # Calculate MD5 hash
    md5_hash = hashlib.md5()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            md5_hash.update(chunk)
    md5_hex = binascii.hexlify(md5_hash.digest()).decode('utf-8')

    # Calculate SHA256 hash
    sha256_hash = hashlib.sha256()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256_hash.update(chunk)
    sha256_hex = binascii.hexlify(sha256_hash.digest()).decode('utf-8')

    # Print the hashes
    print(f"MD5 Hash: {md5_hex}")
    print(f"SHA256 Hash: {sha256_hex}")

    # Return the actual name of the loaded DLL file
    return dll_name

# Example usage:
# dll_name = task_func("path_to_your_dll.dll")
# print(f"Loaded DLL Name: {dll_name}")
import unittest
from unittest.mock import patch
import tempfile
import os
import sys
from io import StringIO
import binascii
class TestCases(unittest.TestCase):
    def setUp(self):
        # Create a temporary DLL file
        self.temp_file = tempfile.NamedTemporaryFile(suffix='.dll', delete=False)
        self.filepath = self.temp_file.name
        # Redirect stdout to capture print statements
        self.original_stdout = sys.stdout
        sys.stdout = StringIO()
    def test_file_existence(self):
        self.assertTrue(os.path.exists(self.filepath))
    def test_invalid_file_path(self):
        with self.assertRaises(OSError):
            task_func('invalid_path.dll')
    @patch('ctypes.CDLL')
    @patch('builtins.open', new_callable=unittest.mock.mock_open, read_data=b'test data')
    @patch('hashlib.md5')
    @patch('hashlib.sha256')
    def test_dll_name_returned(self, mock_sha256, mock_md5, mock_open, mock_cdll):
        """Test if the function returns the name of the loaded DLL file."""
        mock_md5.return_value.digest.return_value = b'\x93\x15\x98\x3f\xcd\xb4\xcc\xcb\x28\x7b\xcc\xdb\xdd\x4e\x8a\x45'  # Mock MD5 digest
        mock_sha256.return_value.digest.return_value = b'\xd7\xa8\xfb\x48\xd2\x8d\x1d\x73\xa0\x34\x6b\xbf\x40\x41\xdf\x98\xc2\x50\x1d\x4a\xe4\x88\x9b\x93\x4f\xaa\x63\xf7\xaf\x67\xe9\xb1'  # Mock SHA256 digest
        mock_cdll.return_value._name = 'test.dll'
        dll_name = task_func(self.filepath)  # Replace 'task_func_module.task_func' with the actual path to your task_func function
        self.assertEqual(dll_name, 'test.dll')
    @patch('ctypes.CDLL')
    @patch('builtins.open', new_callable=unittest.mock.mock_open, read_data=b'test data')
    @patch('hashlib.md5')
    def test_md5_hash_printed(self, mock_md5, mock_open, mock_cdll):
        """Test if the MD5 hash is correctly calculated and printed."""
        expected_hash = b'\x93\x15\x98\x3f\xcd\xb4\xcc\xcb\x28\x7b\xcc\xdb\xdd\x4e\x8a\x45'
        mock_md5.return_value.digest.return_value = expected_hash
        with patch('builtins.print') as mock_print:
            task_func('path/to/test.dll')
            expected_md5_output = f'MD5 Hash: {binascii.hexlify(expected_hash).decode()}'
            mock_print.assert_any_call(expected_md5_output)
    @patch('ctypes.CDLL')
    @patch('builtins.open', new_callable=unittest.mock.mock_open, read_data=b'test data')
    @patch('hashlib.sha256')
    def test_sha256_hash_printed(self, mock_sha256, mock_open, mock_cdll):
        """Test if the SHA256 hash is correctly calculated and printed."""
        expected_hash = b'\xd7\xa8\xfb\x48\xd2\x8d\x1d\x73\xa0\x34\x6b\xbf\x40\x41\xdf\x98\xc2\x50\x1d\x4a\xe4\x88\x9b\x93\x4f\xaa\x63\xf7\xaf\x67\xe9\xb1'
        mock_sha256.return_value.digest.return_value = expected_hash
        with patch('builtins.print') as mock_print:
            task_func('path/to/test.dll')
            expected_sha256_output = f'SHA256 Hash: {binascii.hexlify(expected_hash).decode()}'
            mock_print.assert_any_call(expected_sha256_output)
    def tearDown(self):
        os.remove(self.filepath)
        sys.stdout = self.original_stdout


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)