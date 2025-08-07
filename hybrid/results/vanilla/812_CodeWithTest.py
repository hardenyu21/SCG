import re
from pathlib import Path
import tarfile

# Constants
PATTERN = r"(?<!Distillr)\\\\AcroTray\.exe"
DIRECTORY = r"C:\\SomeDir\\"

def task_func(directory=DIRECTORY, file_pattern=PATTERN):
    # Compile the regular expression pattern
    pattern = re.compile(file_pattern)
    
    # Create a Path object for the directory
    dir_path = Path(directory)
    
    # List to hold paths of files that match the pattern
    matching_files = []
    
    # Iterate over all files in the directory
    for file_path in dir_path.rglob('*'):
        # Check if the file path matches the pattern
        if pattern.search(str(file_path)):
            matching_files.append(file_path)
    
    # If no matching files are found, return None
    if not matching_files:
        return None
    
    # Create a tar file to archive the matching files
    tar_file_path = dir_path / 'archived_files.tar'
    with tarfile.open(tar_file_path, 'w') as tar:
        for file in matching_files:
            tar.add(file, arcname=file.relative_to(dir_path))
    
    # Return the path to the created tar file
    return str(tar_file_path)

# Example usage
# print(task_func())
import unittest
import tempfile
import os
import tarfile
from pathlib import Path
import shutil
class TestCases(unittest.TestCase):
    def setUp(self):
        # Setup directories and files for testing
        self.source_dir = tempfile.mkdtemp()
        self.valid_files = {
            'test1.txt': 'content',
            'test2.doc': 'content',
            'AcroTray.exe': 'content',
            'sample.exe': 'content'
        }
        for filename, content in self.valid_files.items():
            with open(os.path.join(self.source_dir, filename), 'w') as f:
                f.write(content)
        self.test_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.test_dir.cleanup) 
    def create_test_files(self, files):
        """
        Helper function to create test files in the temporary directory.
        """
        for file_name, content in files.items():
            with open(os.path.join(self.test_dir.name, file_name), 'w') as f:
                f.write(content)
    def tearDown(self):
        # Clean up the test directory
        shutil.rmtree(self.source_dir)
    def test_valid_files_archived(self):
        # Setup files that should be archived
        files = {'AcroTray.exe': 'content', 'Ignore.exe': 'ignore this'}
        self.create_test_files(files)
        pattern = r"AcroTray\.exe$"
        
        # Function to test
        tar_file_path = task_func(self.test_dir.name, pattern)
        
        # Verify correct files are archived
        with tarfile.open(tar_file_path, 'r') as tar:
            archived_files = [m.name for m in tar.getmembers()]
            self.assertIn('AcroTray.exe', archived_files)
    def test_no_matches(self):
        # When no files match, the archive should be empty
        tar_file_path = task_func(self.source_dir, r"non_matching_pattern")
        with tarfile.open(tar_file_path, 'r') as tar:
            self.assertEqual(len(tar.getmembers()), 0)
    def test_with_subdirectories(self):
        # Setup files in subdirectories
        sub_dir = Path(self.test_dir.name) / 'subdir'
        sub_dir.mkdir(parents=True, exist_ok=True)
        file_name = 'AcroTray.exe'
        file_path = sub_dir / file_name
        with open(file_path, 'w') as f:
            f.write('content')
        pattern = r"AcroTray\.exe$"
        
        # Function to test
        tar_file_path = task_func(self.test_dir.name, pattern)
        
        # Verify correct files are archived
        with tarfile.open(tar_file_path, 'r') as tar:
            archived_files = [m.name for m in tar.getmembers()]
            self.assertIn(os.path.join('subdir', 'AcroTray.exe'), archived_files)
    def test_empty_directory(self):
        # If the directory is empty, the tar file should also be empty
        empty_dir = tempfile.mkdtemp()
        tar_file_path = task_func(empty_dir, PATTERN)
        with tarfile.open(tar_file_path, 'r') as tar:
            self.assertEqual(len(tar.getmembers()), 0)
        shutil.rmtree(empty_dir)
    def test_file_permission_issues(self):
        # Setup a file with restricted permissions
        file_name = 'AcroTray.exe'
        file_path = os.path.join(self.test_dir.name, file_name)
        with open(file_path, 'w') as f:
            f.write('content')
        os.chmod(file_path, 0o000)  # Make it unreadable
        pattern = r"AcroTray\.exe$"
        
        # Function to test
        tar_file_path = task_func(self.test_dir.name, pattern)
        
        # Verify that files with permission issues are handled
        with tarfile.open(tar_file_path, 'r') as tar:
            archived_files = [m.name for m in tar.getmembers()]
            self.assertNotIn('AcroTray.exe', archived_files)
        os.chmod(file_path, 0o666)  # Restore permissions


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)