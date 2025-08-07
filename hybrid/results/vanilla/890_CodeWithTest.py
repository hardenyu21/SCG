import os
import random
import pandas as pd

def task_func(data_dir,
              csv_files=['file1.csv', 'file2.csv', 'file3.csv'],
              seed=None,
              num_records=10):
    # Set the random seed for reproducibility if provided
    if seed is not None:
        random.seed(seed)
    
    # Randomly select one of the provided csv_files
    selected_file = random.choice(csv_files)
    
    # Construct the full file path
    file_path = os.path.join(data_dir, selected_file)
    
    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {selected_file} does not exist in the directory {data_dir}.")
    
    # Load the CSV file into a DataFrame
    try:
        df = pd.read_csv(file_path)
    except pd.errors.EmptyDataError:
        # Return an empty DataFrame if the file is empty
        return selected_file, pd.DataFrame()
    
    # Check if the DataFrame is empty
    if df.empty:
        return selected_file, pd.DataFrame()
    
    # Randomly select a certain number of records from the DataFrame
    selected_records = df.sample(n=min(num_records, len(df)), random_state=seed)
    
    return selected_file, selected_records
import unittest
import pandas as pd
import os
import tempfile
import shutil
class TestCases(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory
        self.test_dir = tempfile.mkdtemp()
        self.test_files = [
            'file1.csv', 'file2.csv', 'file3.csv', 'file4.csv', 'file5.csv', 'empty.csv'
        ]
        # Sample data for CSV files
        data = {
            'file1.csv': pd.DataFrame({'Name': ['Alice', 'Bob'], 'Age': [25, 30]}),
            'file2.csv': pd.DataFrame({'Name': ['Chris', 'Dana'], 'Age': [35, 40]}),
            'file3.csv': pd.DataFrame({'Name': ['Eve', 'Frank'], 'Age': [45, 50]}),
            'file4.csv': pd.DataFrame({'Name': ['Grace', 'Hank'], 'Age': [55, 60]}),
            'file5.csv': pd.DataFrame({'Name': ['Ivan', 'Julia'], 'Age': [65, 70]}),
            'empty.csv': pd.DataFrame()
        }
        # Create CSV files in the directory
        for file_name, df in data.items():
            df.to_csv(os.path.join(self.test_dir, file_name), index=False)
    def tearDown(self):
        # Remove the directory after the test
        shutil.rmtree(self.test_dir)
    def test_random_selection(self):
        # Testing random selection and ensuring the file chosen and its data are correct
        file_name, df = task_func(self.test_dir, seed=42)
        self.assertTrue(file_name in self.test_files)
        self.assertFalse(df.empty)
    def test_specific_file_selection(self):
        # Test selecting a specific file and checking contents
        file_name, df = task_func(self.test_dir, ['file1.csv'], seed=42)
        expected = pd.read_csv(os.path.join(self.test_dir, 'file1.csv'))
        # Sample from expected and reset index
        expected_sampled = expected.sample(len(df), random_state=42).reset_index(drop=True)
        # Reset index of df to ensure indices match
        df_reset = df.reset_index(drop=True)
        # Assert frame equality
        pd.testing.assert_frame_equal(df_reset, expected_sampled)
    def test_empty_file(self):
        # Ensure an empty file returns an empty DataFrame
        file_name, df = task_func(self.test_dir, ['empty.csv'], seed=42)
        self.assertEqual(file_name, 'empty.csv')
        self.assertTrue(df.empty)
    def test_multiple_files(self):
        # Testing selection from multiple files
        file_name, df = task_func(self.test_dir, ['file3.csv', 'file4.csv'], seed=24)
        self.assertIn(file_name, ['file3.csv', 'file4.csv'])
        self.assertFalse(df.empty)
    def test_no_file_matches(self):
        # Testing behavior when no files match the list
        with self.assertRaises(FileNotFoundError):
            task_func(self.test_dir, ['nonexistent.csv'], seed=42)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)