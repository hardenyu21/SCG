import os
from pathlib import Path
import shutil

def task_func(source_directory: str, target_directory: str) -> int:
    # Define the valid file extensions
    valid_extensions = {'.txt', '.docx', '.xlsx', '.csv'}
    
    # Check if the source directory exists
    if not os.path.exists(source_directory):
        raise FileNotFoundError(f"The source directory '{source_directory}' does not exist.")
    
    # Ensure the target directory exists
    os.makedirs(target_directory, exist_ok=True)
    
    # Initialize a counter for the number of files moved
    files_moved = 0
    
    # Walk through the source directory recursively
    for root, _, files in os.walk(source_directory):
        for file in files:
            # Check if the file has a valid extension
            if Path(file).suffix in valid_extensions:
                # Construct the full path to the source file
                source_file_path = Path(root) / file
                
                # Construct the target file path
                target_file_path = Path(target_directory) / file
                
                # Handle naming conflicts by renaming duplicates
                if target_file_path.exists():
                    # Find a unique name for the file
                    base_name, extension = os.path.splitext(file)
                    counter = 1
                    while target_file_path.exists():
                        new_name = f"{base_name}-{counter}{extension}"
                        target_file_path = Path(target_directory) / new_name
                        counter += 1
                
                # Move the file to the target directory
                shutil.move(str(source_file_path), str(target_file_path))
                files_moved += 1
    
    return files_moved
import unittest
import tempfile
from pathlib import Path
class TestCases(unittest.TestCase):
    def setUp(self):
        self.valid_extensions = [".txt", ".docx", ".xlsx", ".csv"]
    def test_case_1(self):
        # Test with an empty source directory
        with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
            result = task_func(source_dir, target_dir)
            self.assertEqual(
                result, 0, "Should return 0 for an empty source directory."
            )
    def test_case_2(self):
        # Test with a source directory containing only files with no extensions
        with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
            for i in range(3):
                Path(f"{source_dir}/file_{i}").touch()
            result = task_func(source_dir, target_dir)
            self.assertEqual(
                result, 0, "Should return 0 for files with non-matching extensions."
            )
    def test_case_3(self):
        # Test with a source directory containing files with a mix of extensions
        with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
            extensions = self.valid_extensions + [".pdf", ".jpg"]
            for i, ext in enumerate(extensions):
                Path(f"{source_dir}/file_{i}{ext}").touch()
            result = task_func(source_dir, target_dir)
            self.assertTrue(result == len(self.valid_extensions))
    def test_case_4(self):
        # Test with a source directory containing files with all matching extensions
        with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
            for i, ext in enumerate(self.valid_extensions):
                Path(f"{source_dir}/file_{i}{ext}").touch()
            result = task_func(source_dir, target_dir)
            self.assertEqual(
                result, 4, "Should return 4 for all files with matching extensions."
            )
    def test_case_5(self):
        # Test with a source directory containing nested directories with files
        with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
            extensions = [".txt", ".docx", ".xlsx", ".csv"]
            Path(f"{source_dir}/subdir1").mkdir()
            Path(f"{source_dir}/subdir1/subdir2").mkdir()
            for i, ext in enumerate(extensions):
                Path(f"{source_dir}/file_{i}{ext}").touch()
                Path(f"{source_dir}/subdir1/file_{i}{ext}").touch()
                Path(f"{source_dir}/subdir1/subdir2/file_{i}{ext}").touch()
            result = task_func(source_dir, target_dir)
            self.assertEqual(
                result,
                12,
                "Should return 12 for all files in nested directories with matching extensions.",
            )
    def test_case_6(self):
        # Test files with the same name in different subdirectories of the source directory
        with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
            Path(f"{source_dir}/subdir1").mkdir()
            Path(f"{source_dir}/subdir2").mkdir()
            extensions = [".txt", ".docx", ".xlsx", ".csv"]
            # Create files with the same name in different subdirectories
            for ext in extensions:
                (Path(f"{source_dir}/subdir1") / f"file{ext}").touch()
                (Path(f"{source_dir}/subdir2") / f"file{ext}").touch()
            result = task_func(source_dir, target_dir)
            self.assertEqual(
                result,
                8,
                "Should correctly move files with the same name from different source directories.",
            )
    def test_case_7(self):
        # Test handling of invalid path inputs
        source_dir = "/path/does/not/exist"
        with tempfile.TemporaryDirectory() as target_dir:
            with self.assertRaises(FileNotFoundError):
                task_func(source_dir, target_dir)
    def test_case_8(self):
        # Test file renaming when handling duplicate files
        with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
            extensions = self.valid_extensions
            for i, ext in enumerate(extensions):
                filename = f"file_{i}{ext}"
                # Create duplicate files in the source directory
                Path(os.path.join(source_dir, filename)).touch()
                # Create expected duplicate files in the target directory to force renaming
                Path(os.path.join(target_dir, filename)).touch()
            result = task_func(source_dir, target_dir)
            self.assertEqual(result, len(extensions), "Should have moved all files.")
            # Check if files were renamed correctly to avoid overwriting
            expected_files = [f"file_{i}-1{ext}" for i, ext in enumerate(extensions)]
            actual_files = [Path(f).name for f in glob.glob(f"{target_dir}/*")]
            for expected_file in expected_files:
                self.assertIn(
                    expected_file,
                    actual_files,
                    f"{expected_file} was not found in target directory.",
                )


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)