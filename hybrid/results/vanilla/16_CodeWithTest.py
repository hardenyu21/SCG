import os
import glob
import tarfile

def task_func(directory, backup_dir='/path/to/backup'):
    # Check if the specified directory exists
    if not os.path.exists(directory):
        raise FileNotFoundError(f"The specified directory '{directory}' does not exist.")
    
    # Find all .log files in the specified directory
    log_files = glob.glob(os.path.join(directory, '*.log'))
    
    # If no log files are found, return the message
    if not log_files:
        return 'No logs found to backup'
    
    # Ensure the backup directory exists
    os.makedirs(backup_dir, exist_ok=True)
    
    # Define the path for the backup file
    backup_file_path = os.path.join(backup_dir, 'logs_backup.tar.gz')
    
    # Create a tar.gz file and add all log files to it
    with tarfile.open(backup_file_path, 'w:gz') as tar:
        for log_file in log_files:
            tar.add(log_file, arcname=os.path.basename(log_file))
    
    # Delete the original log files after backup
    for log_file in log_files:
        os.remove(log_file)
    
    # Return the path to the backup file
    return backup_file_path
import unittest
import tempfile
import os
import subprocess
import glob
import shutil
class TestCases(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.temp_backup_dir = tempfile.mkdtemp()
        
        # Create some log files and some non-log files
        for i in range(5):
            with open(os.path.join(self.temp_dir, f"file_{i}.log"), "w") as f:
                f.write(f"Mock log content for file_{i}")
            with open(os.path.join(self.temp_dir, f"file_{i}.txt"), "w") as f:
                f.write(f"Mock content for file_{i}.txt")
    def tearDown(self):
        shutil.rmtree(self.temp_dir)
        shutil.rmtree(self.temp_backup_dir)
    def test_backup_creation_and_log_file_deletion(self):
        # Test the creation of the backup file and deletion of original log files.
        backup_path = task_func(self.temp_dir, self.temp_backup_dir)
        self.assertTrue(os.path.exists(backup_path))
        self.assertEqual(backup_path, os.path.join(self.temp_backup_dir, 'logs_backup.tar.gz'))
        self.assertFalse(any(file.endswith('.log') for file in os.listdir(self.temp_dir)))
    def test_no_log_files_to_backup(self):
        # Test behavior when no log files are present in the directory.
        empty_dir = tempfile.mkdtemp()
        result = task_func(empty_dir, self.temp_backup_dir)
        self.assertEqual(result, "No logs found to backup")
        shutil.rmtree(empty_dir)
    def test_non_log_files_remain(self):
        # Ensure that non-log files are not deleted or included in the backup.
        backup_path = task_func(self.temp_dir, self.temp_backup_dir)
        self.assertEqual(len(glob.glob(os.path.join(self.temp_dir, '*.txt'))), 5)  # Check only non-log files remain
    def test_handle_non_existing_directory(self):
        # Verify that a FileNotFoundError is raised for a non-existing source directory.
        with self.assertRaises(FileNotFoundError):
            task_func('/non/existing/directory', self.temp_backup_dir)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)