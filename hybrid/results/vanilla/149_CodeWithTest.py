import pandas as pd
import numpy as np

DEFAULT_COLUMNS = ['Element', 'Count']

def task_func(elements, include_index=False):
    # Calculate the character count for each element
    counts = [len(element) for element in elements]
    
    # Create a dictionary to hold the data
    data = {
        'Element': elements,
        'Count': counts
    }
    
    # If index is to be included, add an 'Index' column
    if include_index:
        data['Index'] = np.arange(len(elements))
        columns = ['Index'] + DEFAULT_COLUMNS
    else:
        columns = DEFAULT_COLUMNS
    
    # Create the DataFrame
    df = pd.DataFrame(data, columns=columns)
    
    return df

# Example usage:
# elements = ["apple", "banana", "cherry"]
# df = task_func(elements, include_index=True)
# print(df)
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        result = task_func(['hello'])
        expected = pd.DataFrame({'Element': ['hello'], 'Count': [5]})
        pd.testing.assert_frame_equal(result, expected)
    def test_case_2(self):
        result = task_func(['a', 'bc', 'def'])
        expected = pd.DataFrame({'Element': ['a', 'bc', 'def'], 'Count': [1, 2, 3]})
        pd.testing.assert_frame_equal(result, expected)
    def test_case_3(self):
        result = task_func(['zzz', 'zzz'])
        expected = pd.DataFrame({'Element': ['zzz', 'zzz'], 'Count': [3, 3]})
        pd.testing.assert_frame_equal(result, expected)
    def test_case_4(self):
        result = task_func(['hello world', 'open ai'])
        expected = pd.DataFrame({'Element': ['hello world', 'open ai'], 'Count': [11, 7]})
        pd.testing.assert_frame_equal(result, expected)
    def test_case_5(self):
        result = task_func(['hello', 'world'], include_index=True)
        expected = pd.DataFrame({'Index': np.array([0, 1], dtype='int64'), 'Element': ['hello', 'world'], 'Count': [5, 5]})
        pd.testing.assert_frame_equal(result, expected)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)