import re
import os
import shutil

def task_func(directory):
    # Define the pattern to search for filenames containing "like" or "what"
    pattern = re.compile(r'like|what', re.IGNORECASE)
    
    # Create the "Interesting Files" subdirectory if it doesn't exist
    interesting_files_dir = os.path.join(directory, "Interesting Files")
    if not os.path.exists(interesting_files_dir):
        os.makedirs(interesting_files_dir)
    
    # List to store the names of files moved
    moved_files = []
    
    # Iterate over all files in the given directory
    for filename in os.listdir(directory):
        # Check if the filename contains "like" or "what"
        if pattern.search(filename):
            # Construct full file paths
            src_file = os.path.join(directory, filename)
            dst_file = os.path.join(interesting_files_dir, filename)
            
            # Move the file to the "Interesting Files" subdirectory
            shutil.move(src_file, dst_file)
            
            # Add the filename to the list of moved files
            moved_files.append(filename)
    
    # Output the list of files moved
    return moved_files
import doctest
import unittest
import tempfile
class TestCases(unittest.TestCase):
    def setUp(self):
        # Setup a clean test environment before each test
        self.base_tmp_dir = tempfile.mkdtemp()
        self.test_directory = f"{self.base_tmp_dir}/test"
        if not os.path.exists(self.test_directory):
            os.makedirs(self.test_directory)
        self.test_files = [
            "file_with_like.txt",
            "another_file_with_what.doc",
            "file_without_keywords.jpg",
            "LIKE_in_caps.pdf",
            "hidden_what_in_name.whatever",
            "no_keyword.png"
        ]
        for file in self.test_files:
            with open(os.path.join(self.test_directory, file), 'w') as f:
                f.write("Dummy content for testing.")
        if os.path.exists(os.path.join(self.test_directory, "Interesting Files")):
            shutil.rmtree(os.path.join(self.test_directory, "Interesting Files"))
    def tearDown(self):
        if os.path.exists(self.test_directory):
            shutil.rmtree(self.test_directory)
    def test_caae_1(self):
        """Test if only files with 'like' or 'what' in their names are moved."""
        expected_files = ["file_with_like.txt", "another_file_with_what.doc", "LIKE_in_caps.pdf", "hidden_what_in_name.whatever"]
        moved_files = task_func(self.test_directory)
        self.assertCountEqual(moved_files, expected_files)
    def test_caae_2(self):
        """Test if 'Interesting Files' directory is created."""
        task_func(self.test_directory)
        self.assertTrue(os.path.exists(os.path.join(self.test_directory, "Interesting Files")))
    def test_caae_3(self):
        """Test that files without 'like' or 'what' in their names are not moved."""
        task_func(self.test_directory)
        remaining_files = os.listdir(self.test_directory)
        expected_remaining = ["file_without_keywords.jpg", "no_keyword.png"]
        self.assertCountEqual(remaining_files, expected_remaining + ["Interesting Files"])
    def test_caae_4(self):
        """Test the case insensitivity of the keyword matching."""
        expected_files = ["LIKE_in_caps.pdf"]
        moved_files = task_func(self.test_directory)
        self.assertIn("LIKE_in_caps.pdf", moved_files)
    def test_caae_5(self):
        """Test the function with an empty directory (should handle gracefully)."""
        empty_dir = os.path.join(self.test_directory, "empty_dir")
        os.makedirs(empty_dir, exist_ok=True)
        result = task_func(empty_dir)
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)