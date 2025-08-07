import os
import pandas as pd

OUTPUT_DIR = './output'

def task_func(df, filename, output_dir=OUTPUT_DIR):
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Construct the full file path
    file_path = os.path.join(output_dir, filename)
    
    # Save the DataFrame to a CSV file
    df.to_csv(file_path, index=False)
    
    # Return the absolute path of the saved CSV file
    return os.path.abspath(file_path)
import unittest
import shutil
import pandas as pd
class TestCases(unittest.TestCase):
    def setUp(self):
        """Create the data directory if it doesn't exist."""
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)
    def tearDown(self):
        """Clean up by removing files created during tests (if any)."""
        shutil.rmtree(OUTPUT_DIR, ignore_errors=True)
    def test_basic_dataframe(self):
        """Test saving a simple DataFrame."""
        df = pd.DataFrame({'A': [1, 2], 'B': ['x', 'y']})
        expected_path = os.path.join(OUTPUT_DIR, 'basic.csv')
        result_path = task_func(df, 'basic.csv')
        self.assertEqual(expected_path[expected_path.rindex('/') + 1:], result_path[result_path.rindex('/') + 1: ])
        self.assertTrue(os.path.exists(result_path))
    def test_with_numeric_and_text(self):
        """Test a DataFrame with both numeric and text columns."""
        df = pd.DataFrame({'Numeric': [10, 20], 'Text': ['Hello', 'World']})
        result_path = task_func(df, 'numeric_text.csv')
        self.assertTrue(os.path.exists(result_path))
    def test_with_special_characters(self):
        """Test a DataFrame containing special characters."""
        df = pd.DataFrame({'Data': ['"Quoted"', ',Comma']})
        result_path = task_func(df, 'special_chars.csv')
        self.assertTrue(os.path.exists(result_path))
    def test_empty_dataframe(self):
        """Test saving an empty DataFrame."""
        df = pd.DataFrame()
        result_path = task_func(df, 'empty.csv')
        self.assertTrue(os.path.exists(result_path))
    def test_returned_path_format(self):
        """Test the format of the returned file path."""
        df = pd.DataFrame({'Column': [1]})
        result_path = task_func(df, 'path_format.csv')
        self.assertTrue(os.path.isabs(result_path))
        self.assertIn('path_format.csv', result_path)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)