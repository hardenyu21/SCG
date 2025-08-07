import os
import shutil

def task_func(src_folder, backup_dir):
    try:
        # Check if the source folder exists
        if not os.path.exists(src_folder):
            raise ValueError(f"The source folder '{src_folder}' does not exist.")
        
        # Ensure the backup directory exists
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)
        
        # Define the backup path
        backup_path = os.path.join(backup_dir, os.path.basename(src_folder))
        
        # Backup the source folder to the backup directory
        shutil.copytree(src_folder, backup_path)
        
        # Delete the source folder
        shutil.rmtree(src_folder)
        
        return True
    except ValueError as ve:
        print(f"ValueError: {ve}")
        return False
    except Exception as e:
        print(f"An error occurred while deleting the source folder: {e}")
        return False
import unittest
import tempfile
import doctest
class TestCases(unittest.TestCase):
    
    def setUp(self):
        # Create a temporary directory for testing
        self.src_folder = tempfile.mkdtemp()
        self.backup_dir = tempfile.mkdtemp()
        
        # Create a sample file in the source folder
        with open(os.path.join(self.src_folder, "sample.txt"), "w") as f:
            f.write("This is a sample file.")
    
    def tearDown(self):
        # Cleanup
        if os.path.exists(self.src_folder):
            shutil.rmtree(self.src_folder)
        if os.path.exists(self.backup_dir):
            shutil.rmtree(self.backup_dir)
    
    def test_case_1(self):
        result = task_func(self.src_folder, self.backup_dir)
        self.assertTrue(result)
        self.assertFalse(os.path.exists(self.src_folder))
        self.assertTrue(os.path.exists(os.path.join(self.backup_dir, os.path.basename(self.src_folder), "sample.txt")))
    
    def test_case_2(self):
        shutil.rmtree(self.src_folder)
        with self.assertRaises(ValueError):
            task_func(self.src_folder, self.backup_dir)
    
    def test_case_3(self):
        os.rmdir(self.backup_dir)
        result = task_func(self.src_folder, self.backup_dir)
        self.assertTrue(result)
        self.assertFalse(os.path.exists(self.src_folder))
        self.assertTrue(os.path.exists(os.path.join(self.backup_dir, os.path.basename(self.src_folder), "sample.txt")))
    
    def test_case_4(self):
        self.assertTrue(task_func(self.src_folder, self.src_folder))
    
    def test_case_5(self):
        os.makedirs(os.path.join(self.backup_dir, os.path.basename(self.src_folder)))
        with self.assertRaises(FileExistsError):
            task_func(self.src_folder, self.backup_dir)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)