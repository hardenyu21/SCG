import pandas as pd
import os

OUTPUT_DIR = './output'

def task_func(df, filename, output_dir=OUTPUT_DIR):
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Construct the full file path
    file_path = os.path.join(output_dir, filename)
    
    # Save the DataFrame to a JSON file
    df.to_json(file_path, orient='records', lines=True)
    
    # Return the full file path
    return file_path
import unittest
import json
import shutil
class TestCases(unittest.TestCase):
    def setUp(self):
        """Set up testing environment; ensure data directory exists."""
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)
    def tearDown(self):
        """Clean up; remove the data directory and its contents after tests."""
        shutil.rmtree(OUTPUT_DIR, ignore_errors=True)
    def test_basic_dataframe(self):
        """Test saving a simple DataFrame."""
        df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
        filepath = task_func(df, 'basic.json')
        with open(filepath, 'r') as f:
            data = json.load(f)
        self.assertEqual(data, [{"A": 1, "B": 3}, {"A": 2, "B": 4}])
    def test_nan_values(self):
        """Test DataFrame with NaN values."""
        df = pd.DataFrame({'A': [1, None], 'B': [None, 4]})
        filepath = task_func(df, 'nan_values.json')
        with open(filepath, 'r') as f:
            data = json.load(f)
        self.assertEqual(data, [{"A": 1, "B": None}, {"A": None, "B": 4}])
    def test_integer_conversion(self):
        """Test converting float to int where applicable."""
        df = pd.DataFrame({'A': [1.0, 2.5], 'B': [3.0, 4.5]})
        filepath = task_func(df, 'int_conversion.json')
        with open(filepath, 'r') as f:
            data = json.load(f)
        self.assertEqual(data, [{"A": 1, "B": 3.0}, {"A": 2.5, "B": 4.5}])
    def test_empty_dataframe(self):
        """Test with an empty DataFrame."""
        df = pd.DataFrame()
        filepath = task_func(df, 'empty.json')
        self.assertTrue(os.path.isfile(filepath))
        with open(filepath, 'r') as f:
            data = json.load(f)
        self.assertEqual(data, [])
    def test_all_nan_dataframe(self):
        """Test DataFrame with all NaN values."""
        df = pd.DataFrame({'A': [None, None], 'B': [None, None]})
        filepath = task_func(df, 'all_nan.json')
        with open(filepath, 'r') as f:
            data = json.load(f)
        self.assertEqual(data, [{"A": None, "B": None}, {"A": None, "B": None}])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)