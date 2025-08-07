import os
import random
import string

def task_func(directory, n_files):
    # Ensure the directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    for i in range(n_files):
        # Generate a random filename
        filename = f"file_{i+1}.txt"
        file_path = os.path.join(directory, filename)
        
        # Generate a random string
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=100))
        
        # Write the random string to the file and reset the cursor
        with open(file_path, 'w+') as file:
            file.write(random_string)
            file.seek(0)
    
    return directory

# Example usage:
# directory_path = task_func('/path/to/directory', 5)
# print(f"Files generated in directory: {directory_path}")
import unittest
import shutil
class TestCases(unittest.TestCase):
    def setUp(self):
        random.seed(42)
        
    def tearDown(self):
        shutil.rmtree('./source', ignore_errors=True)
        shutil.rmtree('./src', ignore_errors=True)
        shutil.rmtree('./s', ignore_errors=True)
    
    def test_case_1(self):
        directory = task_func('./source', 10)
        self.assertTrue(os.path.exists(directory))
        self.assertEqual(len(os.listdir(directory)), 10)
        for file in os.listdir(directory):
            self.assertEqual(file.split('.')[-1], 'txt')
        
    def test_case_2(self):
        directory = task_func('./src', 1)
        self.assertTrue(os.path.exists(directory))
        self.assertEqual(len(os.listdir(directory)), 1)
        for file in os.listdir(directory):
            self.assertEqual(file.split('.')[-1], 'txt')        
        
    def test_case_3(self):
        directory = task_func('./s', 100)
        self.assertTrue(os.path.exists(directory))
        self.assertEqual(len(os.listdir(directory)), 100)
        for file in os.listdir(directory):
            self.assertEqual(file.split('.')[-1], 'txt')        
        
    def test_case_4(self):
        directory = task_func('./s', 0)
        self.assertTrue(os.path.exists(directory))
        self.assertEqual(len(os.listdir(directory)), 0)
        for file in os.listdir(directory):
            self.assertEqual(file.split('.')[-1], 'txt')        
        
    def test_case_5(self):
        directory = task_func('./source', 1)
        self.assertTrue(os.path.exists(directory))
        self.assertEqual(len(os.listdir(directory)), 1)
        for file in os.listdir(directory):
            self.assertEqual(file.split('.')[-1], 'txt')


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)