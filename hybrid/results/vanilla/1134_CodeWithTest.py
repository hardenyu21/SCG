import os
import glob
import hashlib

def task_func(source_dir, target_dir, prefix='#Hash: '):
    # Check if the source directory exists
    if not os.path.exists(source_dir):
        raise FileNotFoundError(f"The source directory '{source_dir}' does not exist.")
    
    # Ensure the target directory exists
    os.makedirs(target_dir, exist_ok=True)
    
    # List to store paths of newly created files
    new_files = []
    
    # Iterate over all files in the source directory
    for file_path in glob.glob(os.path.join(source_dir, '*')):
        if os.path.isfile(file_path):
            # Read the content of the file
            with open(file_path, 'rb') as file:
                content = file.read()
            
            # Compute the MD5 hash of the file content
            md5_hash = hashlib.md5(content).hexdigest()
            
            # Create the new content with the hash prepended
            new_content = (prefix + md5_hash + '\n').encode() + content
            
            # Determine the target file path
            file_name = os.path.basename(file_path)
            target_file_path = os.path.join(target_dir, file_name)
            
            # Write the new content to the target file
            with open(target_file_path, 'wb') as target_file:
                target_file.write(new_content)
            
            # Add the path of the newly created file to the list
            new_files.append(target_file_path)
    
    return new_files
import unittest
import os
import shutil
import tempfile
from unittest.mock import patch
class TestCases(unittest.TestCase):
    def setUp(self):
        # Create temporary directories for source and target
        self.source_dir = tempfile.mkdtemp()
        self.target_dir = tempfile.mkdtemp()
    def tearDown(self):
        # Clean up the directories after tests
        shutil.rmtree(self.source_dir)
        shutil.rmtree(self.target_dir)
    def test_default_directories_and_prefix(self):
        # Create some sample files in source_dir
        sample_files = ['file1.txt', 'file2.txt', 'file3.txt']
        for file_name in sample_files:
            with open(os.path.join(self.source_dir, file_name), 'w') as f:
                f.write("Sample content for " + file_name)
        
        result = task_func(source_dir=self.source_dir, target_dir=self.target_dir)
        expected_files = [os.path.join(self.target_dir, file_name) for file_name in sample_files]
        self.assertListEqual(sorted(result), sorted(expected_files))
        for file in expected_files:
            with open(file, 'r') as f:
                lines = f.readlines()
                self.assertTrue(lines[0].startswith('#Hash: '))
                self.assertIn("Sample content for", ''.join(lines[1:]))
    def test_custom_prefix(self):
        # Testing with a custom prefix
        custom_prefix = "MD5Hash: "
        with open(os.path.join(self.source_dir, "file.txt"), 'w') as f:
            f.write("Sample content")
        
        result = task_func(source_dir=self.source_dir, target_dir=self.target_dir, prefix=custom_prefix)
        for file in result:
            with open(file, 'r') as f:
                lines = f.readlines()
                self.assertTrue(lines[0].startswith(custom_prefix))
    def test_empty_directory(self):
        # Testing with an empty source directory
        result = task_func(source_dir=self.source_dir, target_dir=self.target_dir)
        self.assertEqual(result, [])
    def test_non_existing_source_directory(self):
        # Using a non-existing source directory should raise FileNotFoundError
        non_existing_dir = "/path/to/nonexistent/dir"
        with self.assertRaises(FileNotFoundError):
            task_func(source_dir=non_existing_dir, target_dir=self.target_dir)
    def test_overwriting_existing_files(self):
        # Overwriting existing files in the target directory
        file_path = os.path.join(self.target_dir, "file1.txt")
        with open(file_path, 'w') as f:
            f.write("Initial content.")
        
        with open(os.path.join(self.source_dir, "file1.txt"), 'w') as f:
            f.write("New content.")
        
        task_func(source_dir=self.source_dir, target_dir=self.target_dir)
        with open(file_path, 'r') as f:
            self.assertNotEqual(f.read(), "Initial content.")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)