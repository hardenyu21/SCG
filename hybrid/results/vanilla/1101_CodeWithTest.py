import subprocess
import os
import glob
import time

def task_func(test_dir):
    execution_times = {}
    
    # Ensure the directory exists
    if not os.path.isdir(test_dir):
        raise ValueError(f"The directory {test_dir} does not exist.")
    
    # Find all Python files in the directory
    python_files = glob.glob(os.path.join(test_dir, '*.py'))
    
    for file_path in python_files:
        file_name = os.path.basename(file_path)
        
        # Record the start time
        start_time = time.time()
        
        try:
            # Run the Python script
            subprocess.run(['python', file_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error executing {file_name}: {e}")
        
        # Record the end time
        end_time = time.time()
        
        # Calculate the execution time
        execution_time = end_time - start_time
        
        # Store the execution time in the dictionary
        execution_times[file_name] = execution_time
    
    return execution_times
import unittest
import os
import glob
import time
import shutil
class TestCases(unittest.TestCase):
    def setUp(self):
        self.test_dir = 'testdir_task_func/'
        os.makedirs(self.test_dir, exist_ok=True)
        self.sample_directory = 'testdir_task_func/sample_directory'
        os.makedirs(self.sample_directory, exist_ok=True)
        f = open(self.sample_directory+"/script1.py","w")
        f.write("a <- 42/nA <- a * 2/nprint(a)")
        f.close()
        f = open(self.sample_directory+"/script2.py","w")
        f.write("a <- 42/nA <- a * 2/nprint(a)/nprint(A)")
        f.close()
        f = open(self.sample_directory+"/script3.py","w")
        f.write("a <- 42/nA <- a * 2/nprint(A)")
        f.close()
        self.empty_directory = "testdir_task_func/empty_directory"
        os.makedirs(self.empty_directory, exist_ok=True)
        self.mixed_directory = "testdir_task_func/mixed_directory"
        os.makedirs(self.mixed_directory, exist_ok=True)
        f = open(self.mixed_directory+"/1.txt","w")
        f.write("invalid")
        f.close()
        f = open(self.mixed_directory+"/script4.py","w")
        f.write("print('Hello from script4')")
        f.close()
        self.invalid_directory = "testdir_task_func/invalid_directory"
        os.makedirs(self.invalid_directory, exist_ok=True)
        f = open(self.invalid_directory+"/1.txt","w")
        f.write("invalid")
        f.close()
        
    def tearDown(self):
        # Clean up the test directory
        shutil.rmtree(self.test_dir)
    def test_case_1(self):
        # Testing with the created R scripts directory
        result = task_func(self.sample_directory)
        self.assertEqual(len(result), 3)  # There are 3 R scripts
        self.assertTrue("script1.py" in result)
        self.assertTrue("script2.py" in result)
        self.assertTrue("script3.py" in result)
        for time_taken in result.values():
            self.assertTrue(time_taken >= 0)  # Execution time should be non-negative
    def test_case_2(self):
        # Testing with a non-existent directory (should return an empty dictionary)
        result = task_func("/non/existent/path/")
        self.assertEqual(result, {})
    def test_case_3(self):
        # Testing with a directory that has no Python scripts (should return an empty dictionary)
        empty_dir = self.empty_directory
        os.makedirs(empty_dir, exist_ok=True)
        result = task_func(empty_dir)
        self.assertEqual(result, {})
    def test_case_4(self):
        # Testing with a directory containing other types of files (should return an empty dictionary)
        other_files_dir = self.invalid_directory
        result = task_func(other_files_dir)
        self.assertEqual(result, {})
    def test_case_5(self):
        # Testing with a directory containing a mix of Python scripts and other files
        mix_files_dir = self.mixed_directory
        result = task_func(mix_files_dir)
        self.assertEqual(len(result), 1)  # Only 1 Python script
        self.assertTrue("script4.py" in result)
        for time_taken in result.values():
            self.assertTrue(time_taken >= 0)  # Execution time should be non-negative


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)