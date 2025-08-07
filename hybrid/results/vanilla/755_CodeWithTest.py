import os
import glob

def task_func(directory_path):
    # Get all files in the directory
    files = glob.glob(os.path.join(directory_path, '*'))
    
    new_filenames = []
    
    for file_path in files:
        # Extract the filename from the file path
        filename = os.path.basename(file_path)
        
        # Split the filename into words using period as the separator
        words = filename.split('.')
        
        # Reverse the order of words
        reversed_words = words[::-1]
        
        # Join the reversed words back into a filename
        new_filename = '.'.join(reversed_words)
        
        # Construct the new file path
        new_file_path = os.path.join(directory_path, new_filename)
        
        # Rename the file
        os.rename(file_path, new_file_path)
        
        # Add the new filename to the list
        new_filenames.append(new_filename)
    
    return new_filenames
import unittest
import shutil
import tempfile
class TestCases(unittest.TestCase):
    
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
    def tearDown(self):
        shutil.rmtree(self.test_dir)
    def test_single_file(self):
        open(os.path.join(self.test_dir, "hello.world.txt"), 'a').close()
        new_filenames = task_func(self.test_dir)
        self.assertEqual(new_filenames, ["txt.world.hello"])
    def test_multiple_files(self):
        open(os.path.join(self.test_dir, "sample.data.csv"), 'a').close()
        open(os.path.join(self.test_dir, "test.file.name.jpg"), 'a').close()
        new_filenames = task_func(self.test_dir)
        expected_filenames = ["csv.data.sample", "jpg.name.file.test"]
        self.assertCountEqual(new_filenames, expected_filenames)
    def test_empty_directory(self):
        new_filenames = task_func(self.test_dir)
        self.assertEqual(new_filenames, [])
    def test_files_without_extension(self):
        open(os.path.join(self.test_dir, "file1"), 'a').close()
        open(os.path.join(self.test_dir, "file2.txt"), 'a').close()
        new_filenames = task_func(self.test_dir)
        expected_filenames = ["file1", "txt.file2"]
        self.assertCountEqual(new_filenames, expected_filenames)
    def test_files_with_multiple_extensions(self):
        open(os.path.join(self.test_dir, "file.tar.gz"), 'a').close()
        open(os.path.join(self.test_dir, "archive.zip.001"), 'a').close()
        new_filenames = task_func(self.test_dir)
        expected_filenames = ["gz.tar.file", "001.zip.archive"]
        self.assertCountEqual(new_filenames, expected_filenames)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)