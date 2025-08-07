import re
import os

def task_func(source_dir, target_dir, file_pattern=r'\b[A-Za-z0-9]+\.(txt|doc|docx)\b'):
    # Compile the regular expression pattern
    pattern = re.compile(file_pattern)
    
    # List to store file paths that match the pattern
    matching_files = []
    
    # Walk through the directory
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            # Check if the file name matches the pattern
            if pattern.search(file):
                # Construct the full file path
                file_path = os.path.join(root, file)
                matching_files.append(file_path)
    
    # Create the target directory if it doesn't exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    # Define the path for the configuration file
    config_file_path = os.path.join(target_dir, 'config.txt')
    
    # Write the matching file paths to the configuration file
    with open(config_file_path, 'w') as config_file:
        for file_path in matching_files:
            config_file.write(file_path + '\n')
    
    # Return the path to the created configuration file
    return config_file_path

# Example usage
source_directory = 'C:\\SomeDir\\'
target_directory = 'C:\\ConfigDir\\'
config_file_path = task_func(source_directory, target_directory)
print(f"Configuration file created at: {config_file_path}")
import unittest
import os
import tempfile
import configparser
class TestCases(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for source and target
        self.source_dir = tempfile.mkdtemp()
        self.target_dir = tempfile.mkdtemp()
        # Files that should match the pattern and be moved
        self.valid_files = ['test1.txt', 'document1.doc', 'file1.docx', 'test2.txt', 'notes1.docx']
        for file in self.valid_files:
            with open(os.path.join(self.source_dir, file), 'w') as f:
                f.write("Dummy content")
        # Files that should not match the pattern and remain
        self.invalid_files = ['image1.png', 'script.js', 'data.csv', 'test.tmp', 'archive.zip']
        for file in self.invalid_files:
            with open(os.path.join(self.source_dir, file), 'w') as f:
                f.write("Dummy content")
    def tearDown(self):
        # Clean up by removing directories
        shutil.rmtree(self.source_dir)
        shutil.rmtree(self.target_dir)
    def test_valid_files_moved(self):
        # Test that all valid files are moved
        moved_files_count = task_func(self.source_dir, self.target_dir)
        self.assertEqual(moved_files_count, len(self.valid_files), "Not all valid files were moved.")
    def test_invalid_files_not_moved(self):
        # Test that invalid files are not moved
        task_func(self.source_dir, self.target_dir)
        remaining_files = os.listdir(self.source_dir)
        self.assertListEqual(sorted(remaining_files), sorted(self.invalid_files), "Invalid files were moved.")
    def test_no_files_to_move(self):
        # Test with no files matching the pattern
        # Clean source directory from valid files
        for file in self.valid_files:
            os.remove(os.path.join(self.source_dir, file))
        moved_files_count = task_func(self.source_dir, self.target_dir)
        self.assertEqual(moved_files_count, 0, "Files were moved when none should have.")
    def test_pattern_specificity(self):
        # Test with a more specific pattern that should only match .docx files
        moved_files_count = task_func(self.source_dir, self.target_dir, r'\b[A-Za-z0-9]+\.(docx)\b')
        expected_count = sum(1 for f in self.valid_files if f.endswith('.docx'))
        self.assertEqual(moved_files_count, expected_count, "Pattern did not correctly filter files.")
    def test_target_directory_creation(self):
        # Test that the target directory is created if it does not exist
        shutil.rmtree(self.target_dir)  # Ensure target directory is deleted
        moved_files_count = task_func(self.source_dir, self.target_dir)
        self.assertTrue(os.path.exists(self.target_dir), "Target directory was not created.")
        self.assertEqual(moved_files_count, len(self.valid_files), "Files were not moved correctly when target directory was initially absent.")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)