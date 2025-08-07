import pandas as pd
import os
import time

OUTPUT_DIR = './output'

def task_func(df: pd.DataFrame, filename: str) -> str:
    # Ensure the output directory exists
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    
    # Construct the full file path
    file_path = os.path.join(OUTPUT_DIR, filename)
    
    # Write the DataFrame to a JSON Lines file
    df.to_json(file_path, orient='records', lines=True)
    
    # Return the full path where the file was saved
    return file_path

# Example usage:
# df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
# print(task_func(df, 'data.jsonl'))
import unittest
import pandas as pd
import os
import json
import shutil
class TestCases(unittest.TestCase):
    def setUp(self):
        """Create the data directory if it doesn't exist."""
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)
    def tearDown(self):
        """Clean up by removing the data directory and its contents after tests."""
        shutil.rmtree(OUTPUT_DIR, ignore_errors=True)
    def test_basic_dataframe(self):
        """Ensure basic DataFrame is saved correctly."""
        df = pd.DataFrame({'A': [1, 2], 'B': ['x', 'y']})
        path = task_func(df, 'test_basic.jsonl')
        self.assertTrue(os.path.exists(path))
    def test_empty_dataframe(self):
        """Ensure method handles empty DataFrame correctly."""
        df = pd.DataFrame()
        path = task_func(df, 'test_empty.jsonl')
        self.assertTrue(os.path.exists(path))
    def test_with_nan_values(self):
        """Ensure NaN values are handled correctly."""
        df = pd.DataFrame({'A': [1, None], 'B': [None, 2]})
        path = task_func(df, 'test_nan.jsonl')
        self.assertTrue(os.path.exists(path))
    def test_large_dataframe(self):
        """Test with a large DataFrame."""
        df = pd.DataFrame({'A': range(1000)})
        path = task_func(df, 'test_large.jsonl')
        self.assertTrue(os.path.exists(path))
    def test_special_characters(self):
        """Test DataFrame containing special characters."""
        df = pd.DataFrame({'A': ['Hello, "World"', "It's alright"]})
        path = task_func(df, 'test_special_chars.jsonl')
        self.assertTrue(os.path.exists(path))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)