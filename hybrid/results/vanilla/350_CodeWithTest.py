import subprocess
import os
import shutil
from glob import glob

def task_func(src_folder, dst_folder):
    # Ensure the destination folder exists
    if not os.path.exists(dst_folder):
        os.makedirs(dst_folder)

    # Get all files in the source folder
    files = glob(os.path.join(src_folder, '*'))
    failed_files = []

    for file_path in files:
        if os.path.isfile(file_path):
            try:
                # Compress the file using gzip
                subprocess.run(['gzip', file_path], check=True)
                
                # Get the compressed file path
                compressed_file_path = file_path + '.gz'
                
                # Move the compressed file to the destination folder
                shutil.move(compressed_file_path, dst_folder)
            except subprocess.CalledProcessError:
                failed_files.append(os.path.basename(file_path))
            except Exception as e:
                failed_files.append(os.path.basename(file_path))
                print(f"An error occurred: {e}")

    # Determine if all files were processed successfully
    success = len(failed_files) == 0

    # Prepare the result message
    if success:
        message = "All files were compressed and moved successfully."
    else:
        message = f"Failed to compress or move the following files: {', '.join(failed_files)}"

    # Return the result as a dictionary
    return {
        'success': success,
        'message': message,
        'failed_files': failed_files
    }
import unittest
import doctest
import tempfile
class TestCases(unittest.TestCase):
    def setUp(self):
        self.base_tmp_dir = tempfile.mkdtemp()
        self.src_folder_path = f"{self.base_tmp_dir}/test/source_folder"
        self.dst_folder_path = f"{self.base_tmp_dir}/test/destination_folder"
        
        # Reset the test folders before each test
        os.makedirs(self.src_folder_path, exist_ok=True)
        os.makedirs(self.dst_folder_path, exist_ok=True)
        # Create source and destination folders if they don't exist
        os.makedirs(self.src_folder_path, exist_ok=True)
        os.makedirs(self.dst_folder_path, exist_ok=True)
        # Create some sample files in the source folder
        self.file_contents = ["This is file 1.", "This is file 2.", "This is file 3."]
        file_paths = []
        for idx, content in enumerate(self.file_contents, 1):
            file_path = os.path.join(self.src_folder_path, f"file{idx}.txt")
            with open(file_path, "w") as file:
                file.write(content)
            file_paths.append(file_path)
    def tearDown(self):
        # Reset the test folders after each test
        if os.path.exists(self.base_tmp_dir):
            shutil.rmtree(self.base_tmp_dir, ignore_errors=True)
    def test_case_1(self):
        """Test basic functionality."""
        # Create some sample files in the source folder
        for idx, content in enumerate(self.file_contents, 1):
            file_path = os.path.join(self.src_folder_path, f"file{idx}.txt")
            with open(file_path, "w") as file:
                file.write(content)
        
        result = task_func(self.src_folder_path, self.dst_folder_path)
        self.assertTrue(result['success'])
        self.assertEqual(result['message'], 'All files compressed and moved successfully.')
        self.assertEqual(result['failed_files'], [])
        for idx in range(1, 4):
            self.assertTrue(os.path.exists(os.path.join(self.dst_folder_path, f"file{idx}.txt.gz")))
    def test_case_2(self):
        """Test non-existent source folder."""
        with self.assertRaises(ValueError) as context:
            task_func("/non/existent/path", self.dst_folder_path)
        self.assertEqual(str(context.exception), "Source folder '/non/existent/path' does not exist.")
    def test_case_3(self):
        """Test non-existent destination folder."""
        with self.assertRaises(ValueError) as context:
            task_func(self.src_folder_path, "/non/existent/path")
        self.assertEqual(str(context.exception), "Destination folder '/non/existent/path' does not exist.")
    def test_case_4(self):
        """Test empty source folder."""
        result = task_func(self.src_folder_path, self.dst_folder_path)
        self.assertTrue(result['success'])
        self.assertEqual(result['message'], 'All files compressed and moved successfully.')
        self.assertEqual(result['failed_files'], [])
    
    def test_case_5(self):
        """Test with destination folder having some files."""
        # Create some files in the destination folder
        with open(os.path.join(self.dst_folder_path, "existing_file.txt"), "w") as file:
            file.write("This is an existing file.")
        with open(os.path.join(self.dst_folder_path, "existing_file.txt.gz"), "w") as file:
            file.write("This is an existing compressed file.")
        
        # Create some sample files in the source folder
        for idx, content in enumerate(self.file_contents, 1):
            file_path = os.path.join(self.src_folder_path, f"file{idx}.txt")
            with open(file_path, "w") as file:
                file.write(content)
        
        result = task_func(self.src_folder_path, self.dst_folder_path)
        self.assertTrue(result['success'])
        self.assertEqual(result['message'], 'All files compressed and moved successfully.')
        self.assertEqual(result['failed_files'], [])
        for idx in range(1, 4):
            self.assertTrue(os.path.exists(os.path.join(self.dst_folder_path, f"file{idx}.txt.gz")))
        self.assertTrue(os.path.exists(os.path.join(self.dst_folder_path, "existing_file.txt")))
        self.assertTrue(os.path.exists(os.path.join(self.dst_folder_path, "existing_file.txt.gz")))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)