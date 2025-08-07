import pandas as pd
import os

def task_func(data_dir: str, csv_files: list) -> pd.DataFrame:
    # Check if the list of files is empty
    if not csv_files:
        return pd.DataFrame()
    
    # Initialize an empty list to store DataFrames
    dataframes = []
    
    # Iterate over the list of CSV files
    for file_name in csv_files:
        # Construct the full file path
        file_path = os.path.join(data_dir, file_name)
        
        # Check if the file exists
        if os.path.isfile(file_path):
            # Read the CSV file into a DataFrame and append to the list
            df = pd.read_csv(file_path)
            dataframes.append(df)
        else:
            print(f"Warning: File {file_path} does not exist and will be skipped.")
    
    # Concatenate all DataFrames in the list into a single DataFrame
    merged_df = pd.concat(dataframes, ignore_index=True)
    
    return merged_df
import unittest
import pandas as pd
import os
import shutil
import tempfile
class TestCases(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory to hold CSV files
        self.test_dir = tempfile.mkdtemp()
        self.files = {
            'file1.csv': pd.DataFrame({
                'Name': ['Alice', 'Bob'],
                'Age': [25, 30]
            }),
            'file2.csv': pd.DataFrame({
                'Name': ['Charlie'],
                'Age': [35]
            }),
            'file3.csv': pd.DataFrame({
                'Name': ['David', 'Eve'],
                'Age': [45, 55],
                'Gender': ['Male', 'Female']
            }),
            'file4.csv': pd.DataFrame({
                'Name': ['Faythe'],
                'Animal': ['Cat']
            })
        }
        # Write files to disk
        for filename, df in self.files.items():
            df.to_csv(os.path.join(self.test_dir, filename), index=False)
    def tearDown(self):
        # Clean up the temporary directory
        shutil.rmtree(self.test_dir)
    def test_with_multiple_files(self):
        # Test merging multiple files
        result = task_func(self.test_dir, ['file1.csv', 'file2.csv'])
        expected_df = pd.concat([self.files['file1.csv'], self.files['file2.csv']],
                                ignore_index=True)
        pd.testing.assert_frame_equal(result, expected_df)
    def test_with_different_columns(self):
        # Test files with different columns
        result = task_func(self.test_dir, ['file1.csv', 'file3.csv', 'file4.csv'])
        expected_df = pd.concat([self.files['file1.csv'], self.files['file3.csv'], self.files['file4.csv']],
                                ignore_index=True)
        pd.testing.assert_frame_equal(result, expected_df)
    def test_with_empty_list(self):
        # Test with an empty list of files
        result = task_func(self.test_dir, [])
        self.assertTrue(result.empty)
    def test_with_nonexistent_file(self):
        # Test referencing a non-existent file
        with self.assertRaises(FileNotFoundError):
            task_func(self.test_dir, ['nonexistent.csv'])
    def test_single_file(self):
        # Test with a single file
        result = task_func(self.test_dir, ['file2.csv'])
        expected_df = self.files['file2.csv']
        pd.testing.assert_frame_equal(result, expected_df)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)