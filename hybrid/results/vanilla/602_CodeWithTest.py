import numpy as np
import pandas as pd
import os

# Constants
LETTERS = list('abcdefghijklmnopqrstuvwxyz')
OUTPUT_DIR = './output'

def task_func(file_path, output_dir=OUTPUT_DIR):
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Define the dimensions of the matrix
    rows, cols = 10, 10  # You can change these dimensions as needed
    
    # Generate a 2D matrix with random lowercase letters
    matrix = np.random.choice(LETTERS, size=(rows, cols))
    
    # Create a DataFrame from the matrix
    df = pd.DataFrame(matrix)
    
    # Define the full file path
    full_file_path = os.path.join(output_dir, file_path)
    
    # Write the DataFrame to a CSV file
    df.to_csv(full_file_path, index=False, header=False)

# Example usage
task_func('random_letters.csv')
import unittest
import shutil
import os
class TestCases(unittest.TestCase):
    def setUp(self):
        if not os.path.exists(OUTPUT_DIR):
            os.mkdir(OUTPUT_DIR)
    def tearDown(self):
        """Clean up any files created during the tests."""
        # Check and remove the expected file if it exists
        # if os.path.exists(FILE_PATH):
        #     os.remove(FILE_PATH)
        if os.path.exists(OUTPUT_DIR):
            shutil.rmtree(OUTPUT_DIR)
    def test_case_1(self):
        # Testing with a sample file path
        file_path = os.path.join(OUTPUT_DIR, 'test_output_1.csv')
        task_func(file_path)
        df = pd.read_csv(file_path, sep='\t', header=None)
        self.assertEqual(df.shape, (10, 10), "Matrix shape should be 10x10")
    def test_case_2(self):
        # Testing if the generated matrix contains only lowercase letters
        file_path = os.path.join(OUTPUT_DIR, 'test_output_2.csv')
        task_func(file_path)
        df = pd.read_csv(file_path, sep='\t', header=None)
        all_lower = df.applymap(str.islower).all().all()
        self.assertTrue(all_lower, "All elements should be lowercase letters")
    def test_case_3(self):
        # Testing if the generated matrix contains only letters from the alphabet
        file_path = os.path.join(OUTPUT_DIR, 'test_output_3.csv')
        task_func(file_path)
        df = pd.read_csv(file_path, sep='\t', header=None)
        all_alpha = df.applymap(str.isalpha).all().all()
        self.assertTrue(all_alpha, "All elements should be alphabetic")
    def test_case_4(self):
        # Testing if the generated matrix contains different letters
        file_path = os.path.join(OUTPUT_DIR, 'test_output_4.csv')
        task_func(file_path)
        df = pd.read_csv(file_path, sep='\t', header=None)
        unique_elements = df.nunique().sum()
        self.assertTrue(unique_elements > 10, "Matrix should have more than 10 unique elements")
    def test_case_5(self):
        # Testing if the function overwrites existing files
        file_path = os.path.join(OUTPUT_DIR, 'test_output_5.csv')
        with open(file_path, 'w') as f:
            f.write("test")
        task_func(file_path)
        with open(file_path, 'r') as f:
            content = f.read()
        self.assertNotEqual(content, "test", "Function should overwrite existing content")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)