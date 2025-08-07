import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def task_func(file_name: str) -> pd.DataFrame:
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_name)
    
    # Select only numeric columns
    numeric_cols = df.select_dtypes(include=['number']).columns
    
    # Check if there are any numeric columns
    if len(numeric_cols) == 0:
        raise ValueError("Input does not have numeric columns.")
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Fit and transform the numeric columns
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    
    return df
import unittest
import pandas as pd
import tempfile
import os
import shutil
class TestCases(unittest.TestCase):
    def setUp(self):
        # Set up a temporary directory
        self.test_dir = tempfile.mkdtemp()
    def tearDown(self):
        # Clean up by removing the directory
        shutil.rmtree(self.test_dir)
    def create_csv(self, filename, data):
        # Helper function to create a CSV file with the given data
        full_path = os.path.join(self.test_dir, filename)
        data.to_csv(full_path, index=False)
        return full_path
    def test_non_numeric_and_empty(self):
        # Test with non-numeric and empty data
        non_numeric_df = pd.DataFrame({
            "Name": ["Alice", "Bob"],
            "City": ["New York", "Los Angeles"]
        })
        empty_df = pd.DataFrame()
        non_numeric_path = self.create_csv("non_numeric.csv", non_numeric_df)
        empty_path = self.create_csv("empty.csv", empty_df)
        self.assertRaises(ValueError, task_func, non_numeric_path)
        self.assertRaises(ValueError, task_func, empty_path)
    def test_single_row(self):
        # Test with a single row of numeric data
        single_row_df = pd.DataFrame({
            "Name": ["Olivia Anderson"],
            "Age": [35],
            "Salary": [58000]
        })
        csv_path = self.create_csv("single_row.csv", single_row_df)
        df = task_func(csv_path)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertTrue((df['Age'] == 0).all() and (df['Salary'] == 0).all())
    def test_multiple_rows(self):
        # Test multiple rows with numeric data
        data_df = pd.DataFrame({
            "Name": ["Alice", "Bob", "Charlie"],
            "Age": [25, 35, 45],
            "Salary": [50000, 60000, 70000]
        })
        csv_path = self.create_csv("multiple_rows.csv", data_df)
        df = task_func(csv_path)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertTrue((df['Age'] >= 0).all() and (df['Age'] <= 1).all())
        self.assertTrue((df['Salary'] >= 0).all() and (df['Salary'] <= 1).all())
    def test_mixed_columns(self):
        # Test with a mix of numeric and non-numeric columns
        mixed_df = pd.DataFrame({
            "Name": ["Alice", "Bob", "Charlie"],
            "Age": [25, 35, 45],
            "Salary": [50000, 60000, 70000],
            "City": ["New York", "Chicago", "San Francisco"]
        })
        csv_path = self.create_csv("mixed_columns.csv", mixed_df)
        df = task_func(csv_path)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertTrue((df['Age'] >= 0).all() and (df['Age'] <= 1).all())
        self.assertTrue((df['Salary'] >= 0).all() and (df['Salary'] <= 1).all())
        self.assertTrue('City' in df.columns and df['City'].equals(mixed_df['City']))
    def test_large_dataset(self):
        # Test with a large dataset to ensure scalability
        large_df = pd.DataFrame({
            "Age": range(10000),  # Large range of ages
            "Salary": range(10000, 20000)  # Large range of salaries
        })
        csv_path = self.create_csv("large_dataset.csv", large_df)
        df = task_func(csv_path)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertTrue((df['Age'] >= 0).all() and (df['Age'] <= 1).all())
        self.assertTrue((df['Salary'] >= 0).all() and (df['Salary'] <= 1).all())


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)