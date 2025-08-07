import os
import random

def task_func(directory, n_files):
    # Ensure the directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    for i in range(1, n_files + 1):
        file_name = f'file_{i}.txt'
        file_path = os.path.join(directory, file_name)
        
        # Generate a single digit random integer
        random_digit = random.randint(0, 9)
        
        # Write the random digit to the file
        with open(file_path, 'w') as file:
            file.write(str(random_digit))
        
        # Reset the cursor to the beginning of the file
        with open(file_path, 'r+') as file:
            file.seek(0)
    
    return n_files

# Example usage:
# directory_path = 'path/to/your/directory'
# number_of_files = 5
# task_func(directory_path, number_of_files)
import unittest
import shutil
class TestCases(unittest.TestCase):
    def base(self, dir, n_files, contents):
        random.seed(42)
        # Create directory
        if not os.path.exists(dir):
            os.makedirs(dir)
        # Run function
        n = task_func(dir, n_files)
        # Check files
        self.assertEqual(n, n_files)
        read_data = []
        for f in sorted(os.listdir(dir)):
            self.assertTrue(f.endswith('.txt'))
            with open(os.path.join(dir, f), 'r') as file:
                read_data.append(file.read())
                file.seek(0)
        self.assertEqual(read_data, contents)
    def tearDown(self):
        shutil.rmtree('./directory', ignore_errors=True)
        shutil.rmtree('./dir', ignore_errors=True)
        shutil.rmtree('./d', ignore_errors=True)
    def test_case_1(self):
        self.base('./directory', 5, ['1', '0', '4', '3', '3'])
    def test_case_2(self):
        self.base('./dir', 10, ['1', '9', '0', '4', '3', '3', '2', '1', '8', '1'])
    def test_case_3(self):
        self.base('./d', 15, ['1', '9', '6', '0', '0', '1', '3', '0', '4', '3', '3', '2', '1', '8', '1'])
    def test_case_4(self):
        self.base('./d', 20, ['1', '9', '6', '0', '0', '1', '3', '3', '8', '9', '0', '0', '8', '4', '3', '3', '2', '1', '8', '1'])
    def test_case_5(self):
        self.base('./directory', 25, ['1', '9', '6', '0', '0', '1', '3', '3', '8', '9', '0', '0', '8', '3', '8', '6', '3', '7', '4', '3', '3', '2', '1', '8', '1'])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)