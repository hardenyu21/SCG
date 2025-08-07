import os
import shutil

# Constants
BACKUP_DIR = '/tmp/backup'

def task_func(directory):
    # Check if the backup directory exists
    if not os.path.exists(BACKUP_DIR):
        return f'Backup directory {BACKUP_DIR} does not exist. Cannot rollback update.'
    
    # Construct the backup file path
    backup_file = os.path.join(BACKUP_DIR, os.path.basename(directory) + '.tar.gz')
    
    # Check if the backup file exists
    if not os.path.exists(backup_file):
        return f'Backup file for {directory} does not exist in {BACKUP_DIR}. Cannot rollback update.'
    
    # Check if the target directory exists
    if os.path.exists(directory):
        # Remove the existing directory to prepare for restoration
        shutil.rmtree(directory)
    
    # Extract the backup to the original directory
    try:
        shutil.unpack_archive(backup_file, directory)
    except Exception as e:
        return f'Failed to restore directory {directory} from backup: {str(e)}'
    
    return directory
import unittest
from unittest.mock import patch, MagicMock
import os
import shutil
class TestCases(unittest.TestCase):
    @patch('os.listdir')
    @patch('os.path.exists')
    @patch('shutil.rmtree')
    @patch('shutil.copytree')
    def test_successful_rollback(self, mock_copytree, mock_rmtree, mock_exists, mock_listdir):
        mock_exists.side_effect = lambda x: True if x == BACKUP_DIR else False
        mock_listdir.return_value = ['backup1']
        result = task_func('/tmp/my_data')
        self.assertEqual(result, '/tmp/my_data')
        mock_copytree.assert_called_once()
    @patch('os.listdir')
    @patch('os.path.exists')
    def test_no_backup_directory(self, mock_exists, mock_listdir):
        mock_exists.return_value = False
        result = task_func('/tmp/my_data')
        self.assertEqual(result, 'Backup directory /tmp/backup does not exist. Cannot rollback update.')
    @patch('os.listdir')
    @patch('os.path.exists')
    def test_no_backups_in_backup_directory(self, mock_exists, mock_listdir):
        mock_exists.return_value = True
        mock_listdir.return_value = []
        result = task_func('/tmp/my_data')
        self.assertEqual(result, 'No backups found in /tmp/backup. Cannot rollback update.')
    @patch('os.listdir')
    @patch('os.path.exists')
    @patch('shutil.rmtree')
    @patch('shutil.copytree')
    def test_directory_does_not_exist(self, mock_copytree, mock_rmtree, mock_exists, mock_listdir):
        mock_exists.side_effect = lambda x: True if x == BACKUP_DIR else False
        mock_listdir.return_value = ['backup1']
        result = task_func('/tmp/nonexistent')
        self.assertEqual(result, '/tmp/nonexistent')
        mock_copytree.assert_called_once()
    @patch('os.listdir')
    @patch('os.path.exists')
    @patch('shutil.rmtree')
    @patch('shutil.copytree')
    def test_erroneous_backup_content(self, mock_copytree, mock_rmtree, mock_exists, mock_listdir):
        mock_exists.return_value = True
        mock_listdir.return_value = ['corrupt_backup']
        mock_copytree.side_effect = Exception("Corruption detected")
        with self.assertRaises(Exception) as context:
            task_func('/tmp/my_data')
        self.assertTrue('Corruption detected' in str(context.exception))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)