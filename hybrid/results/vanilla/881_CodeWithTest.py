import pandas as pd
import random

def task_func(csv_file, column_name='data', pattern=r'\d+[xX]', sample_size=None, seed=42):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(csv_file)
    
    # Check if the specified column exists in the DataFrame
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' does not exist in the CSV file.")
    
    # Find rows where the specified column matches the regex pattern
    matches = df[df[column_name].astype(str).str.contains(pattern, regex=True)]
    
    # If sample_size is specified, perform random sampling
    if sample_size is not None:
        if sample_size > len(matches):
            raise ValueError("Sample size cannot be greater than the number of matches.")
        
        # Set the random seed for reproducibility
        random.seed(seed)
        
        # Generate a random sample of indices
        sample_indices = random.sample(range(len(matches)), sample_size)
        
        # Return the sampled DataFrame
        return matches.iloc[sample_indices]
    
    # Return all matches if no sample size is specified
    return matches
import unittest
import pandas as pd
import tempfile
import shutil
import os
class TestCases(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory to store the test CSV files
        self.test_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.test_dir, "test_data.csv")
        # Create a sample DataFrame
        data = {
            "data": ["123x good", "no match here", "456X bad", "789x good", "ABC"],
            "other_column": ["data1", "data2", "data3", "data4", "data5"]
        }
        self.df = pd.DataFrame(data)
        self.df.to_csv(self.test_file, index=False)
    def tearDown(self):
        # Remove temporary directory after the test
        shutil.rmtree(self.test_dir)
    def test_default_parameters(self):
        result = task_func(self.test_file)
        expected_data = {
            "data": ["123x good", "456X bad", "789x good"],
            "other_column": ["data1", "data3", "data4"]
        }
        expected_df = pd.DataFrame(expected_data)
        pd.testing.assert_frame_equal(result.reset_index(drop=True), expected_df)
    def test_custom_column(self):
        with self.assertRaises(KeyError):
            task_func(self.test_file, column_name="nonexistent_column")
    def test_custom_pattern(self):
        result = task_func(self.test_file, pattern='\d+X')
        expected_data = {
            "data": ["456X bad"],
            "other_column": ["data3"]
        }
        expected_df = pd.DataFrame(expected_data)
        pd.testing.assert_frame_equal(result.reset_index(drop=True), expected_df)
    def test_sample_size(self):
        result = task_func(self.test_file, sample_size=2, seed=42)
        self.assertEqual(len(result), 2)
    def test_no_matches(self):
        result = task_func(self.test_file, pattern="nope")
        self.assertTrue(result.empty)
    def test_sample_size_larger_than_matches(self):
        result = task_func(self.test_file, sample_size=10)
        self.assertEqual(len(result), 3)  # Only three matches exist
    def test_zero_sample_size(self):
        result = task_func(self.test_file, sample_size=0)
        self.assertTrue(result.empty)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)