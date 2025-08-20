import unittest
import tempfile
from pathlib import Path

# Global dictionary for user directories
user_directories = {}

def retrieve_user_files(account_id: str, file_path: str) -> Path:
    if account_id in user_directories:
        user_directory = user_directories[account_id]
        file_abs_path = user_directory / file_path
        try:
            file_abs_path.resolve().relative_to(user_directory.resolve())
        except ValueError:
            raise Exception(f"Access to path {file_path} is not allowed")
        if not file_abs_path.exists():
            raise FileNotFoundError(f"File {file_abs_path} does not exist")
        return file_abs_path
    else:
        raise KeyError(f"User {account_id} not found")

class TestRetrieveUserFiles(unittest.TestCase):
    def setUp(self):
        # Create temporary directory structure
        self.temp_dir = tempfile.TemporaryDirectory()
        temp_path = Path(self.temp_dir.name)
        
        # Set up user directories
        self.user1_dir = temp_path / "user1"
        self.user1_dir.mkdir()
        self.user2_dir = temp_path / "user2"
        self.user2_dir.mkdir()
        
        # Create files for user1
        (self.user1_dir / "file1.txt").touch()
        self.subdir = self.user1_dir / "subdir"
        self.subdir.mkdir()
        (self.subdir / "file2.txt").touch()
        
        # Create file for user2
        (self.user2_dir / "secret.txt").touch()
        
        # Configure global user_directories
        global user_directories
        user_directories = {
            "user1": self.user1_dir,
            "user2": self.user2_dir
        }
    
    def tearDown(self):
        # Clean up temporary directory
        self.temp_dir.cleanup()

    def test_existing_file_in_root(self):
        # Happy path: existing user and file in root directory
        result = retrieve_user_files("user1", "file1.txt")
        self.assertEqual(result, self.user1_dir / "file1.txt")

    def test_existing_file_in_subdir(self):
        # Happy path: existing user and file in subdirectory
        result = retrieve_user_files("user1", "subdir/file2.txt")
        self.assertEqual(result, self.subdir / "file2.txt")

    def test_valid_directory_access(self):
        # Happy path: accessing user's home directory
        result = retrieve_user_files("user1", ".")
        self.assertEqual(result, self.user1_dir)

    def test_non_existent_user(self):
        # KeyError: user not found in user_directories
        with self.assertRaises(KeyError):
            retrieve_user_files("user3", "file1.txt")

    def test_non_existent_file(self):
        # FileNotFoundError: file doesn't exist
        with self.assertRaises(FileNotFoundError):
            retrieve_user_files("user1", "missing.txt")

    def test_relative_path_traversal_attempt(self):
        # Exception: relative path escapes user directory
        with self.assertRaises(Exception) as context:
            retrieve_user_files("user1", "../user2/secret.txt")
        self.assertIn("Access to path", str(context.exception))

    def test_absolute_path_traversal_attempt(self):
        # Exception: absolute path escapes user directory
        target_file = self.user2_dir / "secret.txt"
        with self.assertRaises(Exception) as context:
            retrieve_user_files("user1", str(target_file))
        self.assertIn("Access to path", str(context.exception))

    def test_empty_file_path(self):
        # Valid: empty path resolves to user directory
        result = retrieve_user_files("user1", "")
        self.assertEqual(result, self.user1_dir)

    def test_large_account_id(self):
        # Happy path: large account ID
        large_id = "u" * 1000
        user_directories[large_id] = self.user1_dir
        result = retrieve_user_files(large_id, "file1.txt")
        self.assertEqual(result, self.user1_dir / "file1.txt")

    def test_special_characters_in_path(self):
        # Happy path: special characters in file path
        special_file = self.user1_dir / "!@#$%^&().txt"
        special_file.touch()
        result = retrieve_user_files("user1", "!@#$%^&().txt")
        self.assertEqual(result, special_file)


if __name__ == '__main__':
    unittest.main()