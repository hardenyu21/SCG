import pandas as pd
import numpy as np
from random import choice, randint, sample

# Constants
DATA_TYPES = [str, int, float, list, tuple, dict, set]

def generate_random_data(data_type):
    if data_type == str:
        return ''.join(choice('abcdefghijklmnopqrstuvwxyz') for _ in range(5))
    elif data_type == int:
        return randint(0, 9)
    elif data_type == float:
        return float(randint(0, 9))
    elif data_type == list:
        return [randint(0, 9) for _ in range(randint(1, 5))]
    elif data_type == tuple:
        return tuple(randint(0, 9) for _ in range(randint(1, 5)))
    elif data_type == dict:
        return {randint(0, 9): randint(0, 9) for _ in range(randint(1, 5))}
    elif data_type == set:
        return set(sample(range(10), randint(1, 5)))

def task_func(rows, columns):
    data = {f'col{i}': [generate_random_data(choice(DATA_TYPES)) for _ in range(rows)] for i in range(columns)}
    return pd.DataFrame(data)

# Example usage:
# df = task_func(10, 5)
# print(df)
import unittest
class TestCases(unittest.TestCase):
    def setUp(self):
        """Setup a predictable random seed for numpy to ensure deterministic tests."""
        np.random.seed(42)
    def test_dataframe_dimensions(self):
        """Test the generated DataFrame has the correct dimensions."""
        rows, columns = 5, 3
        df = task_func(rows, columns)
        self.assertEqual(df.shape, (rows, columns), "DataFrame should have the specified dimensions.")
    def test_dataframe_data_types(self):
        """Test that each column in the DataFrame has data of the correct type and validates mixed data types."""
        df = task_func(5, 5)
        for col in df.columns:
            values = df[col]
            unique_types = set(type(v) for v in values)
            self.assertTrue(len(unique_types) <= 2, "Each column should contain no more than two distinct data types.")
    def test_dataframe_size(self):
        """Test that the DataFrame has the correct dimensions."""
        rows, columns = 5, 4
        df = task_func(rows, columns)
        self.assertEqual(df.shape, (rows, columns), "DataFrame should have the specified dimensions.")
    def test_column_names(self):
        """Test that the column names are correctly formatted."""
        columns = 3
        df = task_func(5, columns)
        expected_columns = ['col' + str(i) for i in range(columns)]
        self.assertListEqual(list(df.columns), expected_columns, "Column names are not formatted correctly.")
    def test_collection_sizes(self):
        """Test the size constraints of collections like lists, tuples, dicts, and sets."""
        df = task_func(10, 10)
        for col in df.columns:
            if isinstance(df[col][0], (list, tuple, set, dict)):
                if isinstance(df[col][0], dict):
                    sizes = [len(v.keys()) for v in df[col]]
                else:
                    sizes = [len(v) for v in df[col]]
                self.assertTrue(all(1 <= s <= 5 for s in sizes), f"Sizes in column {col} should be between 1 and 5.")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)