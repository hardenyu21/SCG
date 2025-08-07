import os
import shutil
import hashlib

def task_func(ROOT_DIR, DEST_DIR, SPECIFIC_HASH):
    # Ensure the destination directory exists
    if not os.path.exists(DEST_DIR):
        os.makedirs(DEST_DIR)

    # Initialize a counter for the number of files moved
    files_moved = 0

    # Iterate over all files in the root directory
    for root, _, files in os.walk(ROOT_DIR):
        for file in files:
            # Construct the full file path
            file_path = os.path.join(root, file)

            # Calculate the MD5 hash of the file
            with open(file_path, 'rb') as f:
                file_hash = hashlib.md5(f.read()).hexdigest()

            # Check if the file's hash matches the specific hash
            if file_hash == SPECIFIC_HASH:
                # Construct the destination file path
                dest_file_path = os.path.join(DEST_DIR, file)

                # Move the file to the destination directory
                shutil.move(file_path, dest_file_path)

                # Increment the counter
                files_moved += 1

    # Return the number of files moved
    return files_moved
import unittest
import tempfile
import shutil
import os
import hashlib
from pathlib import Path
from unittest.mock import patch
class TestCases(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for ROOT_DIR and DEST_DIR
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root_dir = Path(self.temp_dir.name, 'root')
        self.dest_dir = Path(self.temp_dir.name, 'dest')
        self.root_dir.mkdir()
        self.dest_dir.mkdir()
        
        # Create a dummy file in ROOT_DIR
        file_content = "This is a dummy file."
        self.dummy_file_path = self.root_dir / 'dummy_file.txt'
        with open(self.dummy_file_path, 'w') as f:
            f.write(file_content)
        # Calculate the hash value for the dummy file
        self.dummy_file_hash = hashlib.md5(file_content.encode('utf-8')).hexdigest()
    def tearDown(self):
        # Cleanup the temporary directory
        self.temp_dir.cleanup()
    @patch('shutil.move')
    def test_file_moved_with_matching_hash(self, mock_move):
        """Test that a file is moved when its hash matches the specified hash."""
        result = task_func(str(self.root_dir), str(self.dest_dir), self.dummy_file_hash)
        
        self.assertEqual(result, 1)
        mock_move.assert_called_once()
    def test_no_file_moved_with_non_matching_hash(self):
        """Test no files are moved if hash doesn't match."""
        result = task_func(str(self.root_dir), str(self.dest_dir), 'non_matching_hash')
        
        self.assertEqual(result, 0)
        # Since we're not mocking shutil.move, we verify by checking the files in DEST_DIR
        self.assertEqual(len(list(self.dest_dir.iterdir())), 0)
    def test_dest_dir_created(self):
        """Test that destination directory is created if it doesn't exist."""
        shutil.rmtree(self.dest_dir)  # Remove the dest_dir to test its recreation
        task_func(str(self.root_dir), str(self.dest_dir), 'any_hash')
        
        self.assertTrue(self.dest_dir.exists())
    def test_no_files_to_move(self):
        """Test the function when there are no files to move."""
        os.remove(self.dummy_file_path)  # Remove the dummy file to simulate no files to move
        result = task_func(str(self.root_dir), str(self.dest_dir), 'any_hash')
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)