import os
import re
import pandas as pd

def task_func(pattern: str, directory: str, output_csv: str) -> pd.DataFrame:
    # Compile the regex pattern for efficiency
    regex = re.compile(pattern)
    
    # List to store matched file paths
    matched_paths = []
    
    # Walk through the directory
    for root, _, files in os.walk(directory):
        for file in files:
            # Check if the file name matches the regex pattern
            if regex.match(file):
                # Construct the full file path
                full_path = os.path.join(root, file)
                # Append the matched path to the list
                matched_paths.append(full_path)
    
    # Create a DataFrame from the matched paths
    df = pd.DataFrame(matched_paths, columns=['File Path'])
    
    # Save the DataFrame to a CSV file
    df.to_csv(output_csv, index=False)
    
    # Return the DataFrame
    return df
import unittest
import shutil
OUTPUT_DIR = './output'
class TestCases(unittest.TestCase):
    def setUp(self):
        self.test_dir = OUTPUT_DIR
        if not os.path.exists(self.test_dir):
            os.makedirs(self.test_dir)
        # Create test files
        self.test_file1 = os.path.join(self.test_dir, "test1.txt")
        self.test_file2 = os.path.join(self.test_dir, "ignore.exe")
        with open(self.test_file1, 'w') as f:
            f.write("This is a test file.")
        with open(self.test_file2, 'w') as f:
            f.write("This file should be ignored.")
    def tearDown(self):
        # Remove the test directory and all its contents
        shutil.rmtree(self.test_dir, ignore_errors=True)
    def test_file_matching(self):
        """Ensure function matches correct files."""
        output_csv = os.path.join(self.test_dir, "matched_files.csv")
        df = task_func(r".*\.txt$", self.test_dir, output_csv)
        self.assertTrue(os.path.exists(output_csv))
        self.assertIn(self.test_file1, df['File Path'].values)
    def test_no_files_matched(self):
        """Test when no files match the pattern."""
        output_csv = os.path.join(self.test_dir, "no_match.csv")
        df = task_func(r".*\.md$", self.test_dir, output_csv)
        self.assertTrue(df.empty)
    def test_output_file_creation(self):
        """Ensure the output file is created."""
        output_csv = os.path.join(self.test_dir, "output_creation.csv")
        _ = task_func(r".*\.txt$", self.test_dir, output_csv)
        self.assertTrue(os.path.exists(output_csv))
    def test_correct_number_of_matches(self):
        """Test the number of files matched is correct."""
        output_csv = os.path.join(self.test_dir, "correct_number.csv")
        df = task_func(r".*\.txt$", self.test_dir, output_csv)
        self.assertEqual(len(df), 1)
    def test_pattern_specificity(self):
        """Ensure the regex pattern correctly distinguishes file types."""
        output_csv = os.path.join(self.test_dir, "pattern_specificity.csv")
        df = task_func(r"test1\.txt$", self.test_dir, output_csv)
        self.assertEqual(len(df), 1)
        self.assertIn("test1.txt", df['File Path'].values[0])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)