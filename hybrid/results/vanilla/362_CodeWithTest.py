import pandas as pd
import os

def task_func(original_file_location="test.xlsx", new_file_location="new_test.xlsx", sheet_name="Sheet1"):
    # Check if the original file exists
    if not os.path.exists(original_file_location):
        raise FileNotFoundError(f"The file {original_file_location} does not exist.")
    
    # Read the original Excel file
    try:
        df = pd.read_excel(original_file_location, sheet_name=sheet_name)
    except ValueError as e:
        raise ValueError(f"The specified sheet '{sheet_name}' does not exist in the workbook.") from e
    
    # Write the data to a new Excel file
    df.to_excel(new_file_location, index=False)
    
    # Read the new Excel file to verify contents
    new_df = pd.read_excel(new_file_location, sheet_name=sheet_name)
    
    return new_df
import unittest
import os
import pandas as pd
def create_dummy_excel(file_path='test.xlsx', sheet_name='Sheet1'):
    """
    Creates a dummy Excel file for testing with a specified sheet name and sample data.
    """
    df = pd.DataFrame({'A': [10, 30], 'B': [20, 40]})
    df.to_excel(file_path, index=False, sheet_name=sheet_name)
class TestCases(unittest.TestCase):
    def setUp(self):
        create_dummy_excel()
    def tearDown(self):
        os.remove('test.xlsx')
        if os.path.exists('new_test.xlsx'):
            os.remove('new_test.xlsx')
    def test_normal_functionality(self):
        df = task_func('test.xlsx', 'new_test.xlsx', 'Sheet1')
        
        expect = pd.DataFrame({'A': [10, 30], 'B': [20, 40]})
        self.assertIsInstance(df, pd.DataFrame)
        pd.testing.assert_frame_equal(expect, df)
    def test_non_existent_file(self):
        with self.assertRaises(FileNotFoundError):
            task_func('non_existent.xlsx', 'new_test.xlsx', 'Sheet1')
    def test_invalid_sheet_name(self):
        with self.assertRaises(ValueError):
            task_func('test.xlsx', 'new_test.xlsx', 'NonExistentSheet')
    def test_data_integrity(self):
        df = task_func('test.xlsx', 'new_test.xlsx', 'Sheet1')
        expected_df = pd.DataFrame({'A': [10, 30], 'B': [20, 40]})
        pd.testing.assert_frame_equal(df, expected_df)
    def test_column_names_preserved(self):
        df = task_func('test.xlsx', 'new_test.xlsx', 'Sheet1')
        self.assertListEqual(list(df.columns), ['A', 'B'])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)