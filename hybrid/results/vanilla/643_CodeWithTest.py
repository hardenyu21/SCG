import re
import pandas as pd
import numpy as np

# Constants
DATA_PATTERN = r'>\d+\.\d+<'

def task_func(dataframe, data_pattern=DATA_PATTERN):
    """
    Extract numeric data from a Pandas DataFrame based on a specific pattern.
    
    Parameters:
    - dataframe: pd.DataFrame - The input DataFrame to process.
    - data_pattern: str - The regex pattern to search for in each cell.
    
    Returns:
    - pd.DataFrame: A modified DataFrame with cells containing the extracted numeric values or NaN.
    """
    def extract_number(cell):
        match = re.search(data_pattern, cell)
        if match:
            # Extract the number from the matched pattern
            return float(match.group(0)[1:-1])
        else:
            return np.nan
    
    # Apply the extraction function to each element in the DataFrame
    modified_df = dataframe.applymap(extract_number)
    
    return modified_df

# Example usage:
# df = pd.DataFrame({
#     'A': ['>1.23<', 'text', '>4.56<'],
#     'B': ['>7.89<', '>0.12<', 'no match']
# })
# result = task_func(df)
# print(result)
import unittest
class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        df = pd.DataFrame({'A': ['>1.23<', '>4.56<'], 'B': ['>7.89<', '>0.12<']})
        result = task_func(df)
        expected = pd.DataFrame({'A': [1.23, 4.56], 'B': [7.89, 0.12]})
        pd.testing.assert_frame_equal(result, expected)
    
    def test_case_2(self):
        df = pd.DataFrame({'A': ['1.23', '4.56'], 'B': ['7.89', '0.12']})
        result = task_func(df)
        expected = pd.DataFrame({'A': [np.nan, np.nan], 'B': [np.nan, np.nan]})
        pd.testing.assert_frame_equal(result, expected)
    
    def test_case_3(self):
        df = pd.DataFrame({'A': ['>1.23<', '4.56'], 'B': ['>7.89<', '0.12']})
        result = task_func(df)
        expected = pd.DataFrame({'A': [1.23, np.nan], 'B': [7.89, np.nan]})
        pd.testing.assert_frame_equal(result, expected)
    
    def test_case_4(self):
        df = pd.DataFrame({'A': ['>1.23<', None], 'B': [None, '>0.12<']})
        result = task_func(df)
        expected = pd.DataFrame({'A': [1.23, np.nan], 'B': [np.nan, 0.12]})
        pd.testing.assert_frame_equal(result, expected)
    
    def test_case_5(self):
        df = pd.DataFrame()
        result = task_func(df)
        expected = pd.DataFrame()
        pd.testing.assert_frame_equal(result, expected)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)