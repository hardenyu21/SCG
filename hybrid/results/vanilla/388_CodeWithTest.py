import collections
import pandas as pd
import os

def task_func(my_tuple, path_csv_files):
    # Initialize a dictionary to store the results
    result = {column: collections.defaultdict(int) for column in my_tuple}
    
    # Iterate over each file in the specified directory
    for filename in os.listdir(path_csv_files):
        if filename.endswith('.csv'):
            file_path = os.path.join(path_csv_files, filename)
            # Read the CSV file into a DataFrame
            df = pd.read_csv(file_path)
            
            # Iterate over each specified column
            for column in my_tuple:
                if column in df.columns:
                    # Count occurrences of each value in the column
                    value_counts = df[column].value_counts()
                    # Update the result dictionary with these counts
                    for value, count in value_counts.items():
                        result[column][value] += count
    
    # Convert defaultdicts to regular dicts for the final output
    result = {column: dict(counts) for column, counts in result.items()}
    
    return result
import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
class TestCases(unittest.TestCase):
    @patch('pandas.read_csv')
    def test_read_csv_files(self, mock_read_csv):
        # Mocking pandas.read_csv to return a DataFrame
        mock_read_csv.side_effect = lambda x: pd.DataFrame({'Country': ['USA', 'Canada', 'USA'], 'Gender': ['Male', 'Female', 'Male']})
        # Call the function with mocked data
        result = task_func(('Country', 'Gender'), ['file1.csv'])
        # Assertions to verify the function behavior
        self.assertEqual(result['Country'], {'USA': 2, 'Canada': 1})
        self.assertEqual(result['Gender'], {'Male': 2, 'Female': 1})
   
    @patch('pandas.read_csv')
    def test_empty_csv_files(self, mock_read_csv):
        # Mocking pandas.read_csv to return an empty DataFrame
        mock_read_csv.side_effect = lambda x: pd.DataFrame(columns=['Country', 'Gender'])
        # Call the function with mocked data
        result = task_func(('Country', 'Gender'), ['file1.csv'])
        # Assertions to verify the function behavior
        self.assertEqual(result['Country'], {})
        self.assertEqual(result['Gender'], {})
    @patch('pandas.read_csv')
    def test_missing_column(self, mock_read_csv):
        # Mocking pandas.read_csv to return a DataFrame with missing 'Gender' column
        mock_read_csv.side_effect = lambda x: pd.DataFrame({'Country': ['USA', 'Canada', 'USA']})
        # Call the function with mocked data
        result = task_func(('Country', 'Gender'), ['file1.csv', 'file2.csv'])
        # Assertions to verify the function behavior
        self.assertEqual(result['Country'], {'USA': 4, 'Canada': 2})
        self.assertEqual(result['Gender'], {})
    @patch('pandas.read_csv')
    def test_no_csv_files(self, mock_read_csv):
        # Call the function with mocked data
        result = task_func(('Country', 'Gender'), [])
        # Assertions to verify the function behavior
        self.assertEqual(result['Country'], {})
        self.assertEqual(result['Gender'], {})
    @patch('pandas.read_csv')
    def test_invalid_csv_files(self, mock_read_csv):
        # Mocking pandas.read_csv to raise an exception when reading the CSV files
        mock_read_csv.side_effect = Exception
        # Call the function with mocked data
        with self.assertRaises(Exception):
            result = task_func(('Country', 'Gender'), ['file3.csv'])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)