import os
import shutil
import tempfile

# Constants
BACKUP_DIR = '/tmp/backup'

def get_unique_backup_dir():
    # Create a unique backup directory path
    return tempfile.mkdtemp(dir=BACKUP_DIR)

def task_func(directory):
    errors = []
    backup_dir = None

    try:
        # Ensure the backup directory exists
        os.makedirs(BACKUP_DIR, exist_ok=True)

        # Get a unique backup directory path
        backup_dir = get_unique_backup_dir()

        # Copy the directory to the backup location
        shutil.copytree(directory, backup_dir)

        # Clean the original directory
        for root, dirs, files in os.walk(directory, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(directory)

    except Exception as e:
        errors.append(str(e))

    return backup_dir, errors

# Example usage:
# backup_path, errors = task_func('/path/to/directory')
# print(f"Backup Path: {backup_path}")
# print(f"Errors: {errors}")
import os
import shutil
import unittest
from unittest import TestCase, main
from unittest.mock import patch, MagicMock
class TestCases(unittest.TestCase):
    @patch('os.makedirs')
    @patch('shutil.copytree')
    @patch('shutil.rmtree')
    @patch('os.listdir', return_value=['data.json'])
    @patch('os.path.exists', return_value=True)
    def test_backup_and_clean(self, mock_exists, mock_listdir, mock_rmtree, mock_copytree, mock_makedirs):
        backup_dir, errors = task_func('/fake/source')
        mock_copytree.assert_called_once()
        self.assertFalse(errors)
    @patch('os.listdir', return_value=[])
    @patch('os.path.exists', return_value=False)
    def test_no_files_to_move(self, mock_exists, mock_listdir):
        backup_dir, errors = task_func('/fake/source')
        self.assertIn('Directory does not exist: /fake/source', errors)
    @patch('os.makedirs')
    @patch('shutil.copytree', side_effect=shutil.Error("Copy failed"))
    @patch('shutil.rmtree')
    @patch('os.listdir', return_value=['data.json'])
    @patch('os.path.exists', return_value=True)
    def test_backup_failure(self, mock_exists, mock_listdir, mock_rmtree, mock_copytree, mock_makedirs):
        backup_dir, errors = task_func('/fake/source')
        self.assertIsNotNone(errors)
        self.assertIn("Copy failed", errors)
    @patch('os.makedirs')
    @patch('shutil.copytree')
    @patch('shutil.rmtree', side_effect=PermissionError("Permission denied"))
    @patch('os.listdir', return_value=['data.json'])
    @patch('os.path.exists', return_value=True)
    def test_cleanup_failure(self, mock_exists, mock_listdir, mock_rmtree, mock_copytree, mock_makedirs):
        backup_dir, errors = task_func('/fake/source')
        self.assertTrue(any("Permission denied" in error for error in errors))
    @patch(__name__ + '.get_unique_backup_dir')  # Patch using the current module name
    @patch('os.makedirs')
    @patch('shutil.copytree')
    @patch('shutil.rmtree')
    @patch('os.listdir', return_value=['large_data.json', 'large_data_2.json'])
    @patch('os.path.exists', return_value=True)
    def test_large_files_backup(self, mock_exists, mock_listdir, mock_rmtree, mock_copytree, mock_makedirs, mock_unique_backup_dir):
        # Mock the unique backup directory function to return a predictable result
        expected_backup_dir = '/fake/backup/path'
        mock_unique_backup_dir.return_value = expected_backup_dir
        # Simulate the function call
        backup_dir, errors = task_func('/fake/source')
        # Assertions to verify the functionality
        mock_copytree.assert_called_once()
        self.assertFalse(errors)
        self.assertEqual(backup_dir, expected_backup_dir)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)