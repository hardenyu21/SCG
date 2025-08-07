import re
import pandas as pd

def task_func(df: pd.DataFrame) -> int:
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame")
    
    # Define the pattern to match brackets
    pattern = r'[(){}[\]]'
    
    # Initialize a counter for brackets
    total_brackets = 0
    
    # Iterate over each element in the DataFrame
    for column in df.columns:
        for value in df[column]:
            # Convert the value to string and find all matches of the pattern
            if isinstance(value, str):
                matches = re.findall(pattern, value)
                # Increment the counter by the number of matches
                total_brackets += len(matches)
    
    return total_brackets

# Example usage
df = pd.DataFrame({'Test': ['(a)', 'b', '[[[[))c']})
print(task_func(df))  # Output: 8
import unittest
import pandas as pd
from faker import Faker
fake = Faker()
class TestCases(unittest.TestCase):
    def test_wrong_input(self):
        # test with non dataframe input
        self.assertRaises(Exception, task_func, 1)
        self.assertRaises(Exception, task_func, ['a'])
        self.assertRaises(Exception, task_func, {'a': 1})
        self.assertRaises(Exception, task_func, 'asdf')
    def test_case_1(self):
        # Test with DataFrame containing no brackets
        df = pd.DataFrame({
            'A': [fake.word() for _ in range(5)],
            'B': [fake.word() for _ in range(5)]
        })
        result = task_func(df)
        self.assertEqual(result, 0)
    def test_case_2(self):
        # Test with DataFrame containing a few brackets
        df = pd.DataFrame({
            'A': ['(a)', 'b', 'c', '{d}', 'e'],
            'B': ['f', '[g]', 'h', 'i', 'j']
        })
        result = task_func(df)
        self.assertEqual(result, 6)
    def test_case_3(self):
        # Test with DataFrame where every entry contains a bracket
        df = pd.DataFrame({
            'A': ['(a)', '{b}', '[c]', '(d)', '[e]'],
            'B': ['{f}', '(g)', '[h]', '{i}', '(j)']
        })
        result = task_func(df)
        self.assertEqual(result, 20)
    def test_case_4(self):
        # Test with DataFrame containing mixed characters and brackets
        df = pd.DataFrame({
            'A': ['(a1)', '{b2}', 'c3', 'd4', '[e5]'],
            'B': ['f6', 'g7', '[h8]', 'i9', 'j0']
        })
        result = task_func(df)
        self.assertEqual(result, 8)
    def test_case_5(self):
        # Test with DataFrame containing numbers, letters, and brackets
        df = pd.DataFrame({
            'A': ['(123]', '{{456}', '789', '0ab', '[cde]'],
            'B': ['fgh', 'ijk', '[)lmn]', 'opq', 'rst']
        })
        result = task_func(df)
        self.assertEqual(result, 10)
    def test_empty(self):
        # test with empty df
        df = pd.DataFrame()
        result = task_func(df)
        self.assertEqual(result, 0)
    def test_only(self):
        # test df with only parenthesis as entries
        df = pd.DataFrame({
            'test': ['[[()]', '{}{{{{{{))))}}', '[]'],
            'asdf': ['{]', '()))', '))}}]]']
        })
        result = task_func(df)
        self.assertEqual(result, 33)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)