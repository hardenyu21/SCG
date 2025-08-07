import os
import pandas as pd
import numpy as np

def task_func(data_dir: str, csv_file: str) -> pd.DataFrame:
    # Construct the full file path
    file_path = os.path.join(data_dir, csv_file)
    
    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {csv_file} does not exist in the directory {data_dir}.")
    
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    
    # If the DataFrame is empty, return it as is
    if df.empty:
        return df
    
    # Replace NaN values in numeric columns with the mean of the column
    for column in df.select_dtypes(include=[np.number]).columns:
        mean_value = df[column].mean()
        df[column].fillna(mean_value, inplace=True)
    
    return df
import unittest
import pandas as pd
import numpy as np
import os
import tempfile
import shutil
class TestCases(unittest.TestCase):
    def setUp(self):
        self.folder_path = 'task_func_data'
    def setUp(self):
        # Create a temporary directory for test data
        self.test_dir = tempfile.mkdtemp()
    def tearDown(self):
        # Remove the temporary directory after the test
        shutil.rmtree(self.test_dir)
    def create_csv(self, filename, data):
        # Helper method to create a CSV file
        filepath = os.path.join(self.test_dir, filename)
        data.to_csv(filepath, index=False)
        return filename
    def test_empty_csv(self):
        # Test with an empty CSV file
        filename = self.create_csv('empty.csv', pd.DataFrame())
        result = task_func(self.test_dir, filename)
        self.assertTrue(result.empty)
    def test_numeric_columns_nan_replacement(self):
        data = pd.DataFrame({
            'Age': [25, np.nan, 30],
            'Salary': [50000, 60000, np.nan]
        })
        filename = self.create_csv('data.csv', data)
        expected = pd.DataFrame({
            'Age': [25.0, 27.5, 30.0],  # Ensure all ages are floats
            'Salary': [50000.0, 60000.0, 55000.0]  # Ensure all salaries are floats
        })
        result = task_func(self.test_dir, filename)
        pd.testing.assert_frame_equal(result, expected)
    def test_mixed_columns(self):
        data = pd.DataFrame({
            'Name': ['Alice', 'Bob', 'Charlie'],
            'Score': [np.nan, 88, 92]
        })
        filename = self.create_csv('mixed.csv', data)
        expected = pd.DataFrame({
            'Name': ['Alice', 'Bob', 'Charlie'],
            'Score': [90.0, 88.0, 92.0]  # Ensure all scores are floats
        })
        result = task_func(self.test_dir, filename)
        pd.testing.assert_frame_equal(result, expected)
    def test_all_nan_column(self):
        # Test with a column that is entirely NaN
        data = pd.DataFrame({
            'Empty': [np.nan, np.nan, np.nan]
        })
        filename = self.create_csv('all_nan.csv', data)
        result = task_func(self.test_dir, filename)
        self.assertTrue(result['Empty'].isnull().all())
    def test_no_numeric_data(self):
        # Test a CSV file with no numeric data
        data = pd.DataFrame({
            'City': ['New York', 'Los Angeles', 'Chicago']
        })
        filename = self.create_csv('cities.csv', data)
        result = task_func(self.test_dir, filename)
        pd.testing.assert_frame_equal(result, data)
    def test_file_not_found(self):
        # Test the FileNotFoundError
        with self.assertRaises(FileNotFoundError):
            task_func(self.test_dir, "non_existent.csv")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)