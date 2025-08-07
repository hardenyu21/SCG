import pandas as pd
import numpy as np

def task_func(d):
    # Check if the input is a list of dictionaries
    if not isinstance(d, list) or not all(isinstance(item, dict) for item in d):
        raise ValueError("Input must be a list of dictionaries.")
    
    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(d)
    
    # Check if the DataFrame contains the required keys
    required_keys = {'x', 'y', 'z'}
    if not required_keys.issubset(df.columns):
        raise ValueError("Input dictionaries must contain the keys 'x', 'y', and 'z'.")
    
    # Calculate statistics for each key
    statistics = {}
    for key in required_keys:
        stats = {
            'mean': df[key].mean(),
            'sum': df[key].sum(),
            'max': df[key].max(),
            'min': df[key].min(),
            'std': df[key].std()
        }
        statistics[key] = stats
    
    return statistics
# Test suite
import unittest
class TestCases(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(task_func([]), {'x': None, 'y': None, 'z': None})
    def test_valid_input(self):
        data = [{'x': 1, 'y': 10, 'z': 5}, {'x': 3, 'y': 15, 'z': 6}, {'x': 2, 'y': 1, 'z': 7}]
        result = task_func(data)
        self.assertAlmostEqual(result['x']['mean'], 2.0)
        self.assertAlmostEqual(result['y']['mean'], 8.666666666666666)
        self.assertAlmostEqual(result['z']['mean'], 6.0)
    def test_invalid_input_type(self):
        with self.assertRaises(ValueError):
            task_func("not a list")
    def test_partial_keys(self):
        data = [{'x': 1, 'y': 2}, {'y': 3, 'z': 4}]
        result = task_func(data)
        self.assertIsNotNone(result['x'])
        self.assertIsNotNone(result['y'])
        self.assertIsNotNone(result['z'])
    def test_all_keys_missing(self):
        data = [{'a': 1}, {'b': 2}]
        self.assertEqual(task_func(data), {'x': None, 'y': None, 'z': None})


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)