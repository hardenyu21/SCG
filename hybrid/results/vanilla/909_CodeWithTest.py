import pandas as pd
import itertools
from random import shuffle

def task_func(letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'], categories=['Category 1', 'Category 2', 'Category 3']):
    # Create a list of categories repeated enough times to match the number of letters
    repeated_categories = list(itertools.islice(itertools.cycle(categories), len(letters)))
    
    # Shuffle the categories to randomize the association
    shuffle(repeated_categories)
    
    # Create a DataFrame with the letters and their associated categories
    df = pd.DataFrame({
        'Letter': letters,
        'Category': repeated_categories
    })
    
    return df

# Example usage
df = task_func()
print(df)
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Testing with default parameters
        df = task_func()
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertEqual(set(df.columns), {'Letter', 'Category'})
        self.assertEqual(len(df), 27)  # 9 letters * 3 categories
    def test_case_2(self):
        # Testing with custom parameters
        df = task_func(['X', 'Y'], ['Cat 1'])
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertEqual(set(df.columns), {'Letter', 'Category'})
        self.assertEqual(len(df), 2)  # 2 letters * 1 category
    def test_case_3(self):
        # Testing with empty categories list
        df = task_func(['X', 'Y'], [])
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertEqual(set(df.columns), {'Letter', 'Category'})
        self.assertEqual(len(df), 0)  # 2 letters * 0 categories
    def test_case_4(self):
        # Testing with empty letters list
        df = task_func([], ['Cat 1', 'Cat 2'])
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertEqual(set(df.columns), {'Letter', 'Category'})
        self.assertEqual(len(df), 0)  # 0 letters * 2 categories
    def test_case_5(self):
        # Testing with both empty lists
        df = task_func([], [])
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertEqual(set(df.columns), {'Letter', 'Category'})
        self.assertEqual(len(df), 0)  # 0 letters * 0 categories


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)