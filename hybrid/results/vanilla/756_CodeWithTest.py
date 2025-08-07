import shutil
from pathlib import Path
from typing import List

def task_func(source_dir: str, target_dir: str, extensions: List[str]) -> int:
    # Convert source_dir and target_dir to Path objects
    source_path = Path(source_dir)
    target_path = Path(target_dir)
    
    # Check if source_dir and target_dir exist
    if not source_path.exists() or not source_path.is_dir():
        raise ValueError(f"Source directory '{source_dir}' does not exist.")
    if not target_path.exists() or not target_path.is_dir():
        raise ValueError(f"Target directory '{target_dir}' does not exist.")
    
    # Initialize a counter for moved files
    moved_files_count = 0
    
    # Iterate over all files in the source directory
    for file in source_path.iterdir():
        # Check if the file has one of the specified extensions
        if file.is_file() and file.suffix in extensions:
            # Move the file to the target directory
            shutil.move(str(file), target_path / file.name)
            # Increment the counter
            moved_files_count += 1
    
    # Return the number of moved files
    return moved_files_count
import unittest
import tempfile
import os
import shutil
def setup_test_environment(extensions, num_files_per_extension):
    # Create temporary directories
    source_dir = tempfile.mkdtemp()
    target_dir = tempfile.mkdtemp()
    file_list = []
    # Populate source_dir with files
    for ext in extensions:
        for i in range(num_files_per_extension):
            with open(os.path.join(source_dir, f"file_{i}{ext}"), "w") as f:
                f.write(f"This is a sample {ext} file.")
                file_list.append(f"file_{i}{ext}")
    return source_dir, target_dir, file_list
# Cleanup function to remove temporary directories after test
def cleanup_test_environment(source_dir, target_dir):
    shutil.rmtree(source_dir)
    shutil.rmtree(target_dir)
# Define the test cases
class TestCases(unittest.TestCase):
    def test_case_dir(self):
        source_dir, target_dir, file_list = setup_test_environment(['.jpg', '.png', '.gif'], 3)
        self.assertRaises(Exception, task_func, 'non_existent', target_dir, ['.test'])
        self.assertRaises(Exception, task_func, source_dir, 'non_existent', ['.test'])
    
    def test_case_1(self):
        # Test basic functionality with jpg, png, and gif extensions
        source_dir, target_dir, file_list = setup_test_environment(['.jpg', '.png', '.gif'], 3)
        result = task_func(source_dir, target_dir, ['.jpg', '.png', '.gif'])
        self.assertEqual(result, 9)  # 3 files for each of the 3 extensions
        self.assertEqual(len(os.listdir(target_dir)), 9)
        self.assertCountEqual(file_list, os.listdir(target_dir))
        cleanup_test_environment(source_dir, target_dir)
    def test_case_2(self):
        # Test only one extension
        source_dir, target_dir, file_list = setup_test_environment(['.jpg', '.png', '.gif', '.txt'], 12)
        result = task_func(source_dir, target_dir, ['.jpg'])
        file_list = [file for file in file_list if file[-4:] == '.jpg']
        self.assertEqual(result, 12)  # Only jpg files should be moved
        self.assertEqual(len(os.listdir(target_dir)), 12)
        self.assertCountEqual(file_list, os.listdir(target_dir))
        cleanup_test_environment(source_dir, target_dir)
    def test_case_3(self):
        # Test with no files to move
        source_dir, target_dir, file_list = setup_test_environment(['.jpg'], 8)
        result = task_func(source_dir, target_dir, ['.png'])
        self.assertEqual(result, 0)  # No png files in source
        self.assertEqual(len(os.listdir(target_dir)), 0)
        self.assertCountEqual([], os.listdir(target_dir))
        cleanup_test_environment(source_dir, target_dir)
    def test_case_4(self):
        # Test with empty source directory
        source_dir = tempfile.mkdtemp()
        target_dir = tempfile.mkdtemp()
        result = task_func(source_dir, target_dir, ['.jpg', '.png', '.gif'])
        self.assertEqual(result, 0)  # No files to move
        self.assertEqual(len(os.listdir(target_dir)), 0)
        self.assertCountEqual([], os.listdir(target_dir))
        cleanup_test_environment(source_dir, target_dir)
    def test_case_5(self):
        # Test moving multiple extensions but not all
        source_dir, target_dir, file_list = setup_test_environment(['.jpg', '.txt', '.doc', 'png'], 5)
        result = task_func(source_dir, target_dir, ['.jpg', '.txt', '.doc'])
        file_list = [file for file in file_list if file[-4:] in ['.jpg', '.txt', '.doc']]
        self.assertEqual(result, 15)  # All files should be moved
        self.assertEqual(len(os.listdir(target_dir)), 15)
        self.assertCountEqual(file_list, os.listdir(target_dir))
        cleanup_test_environment(source_dir, target_dir)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)