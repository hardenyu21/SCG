import pandas as pd
from collections import Counter

def task_func(d):
    # Initialize a dictionary to hold Counter objects for each key
    result = {'x': Counter(), 'y': Counter(), 'z': Counter()}
    
    # Iterate over each dictionary in the list
    for item in d:
        # Update the Counter for each key if it exists in the current dictionary
        for key in result:
            if key in item:
                result[key].update([item[key]])
    
    return result

# Example usage:
# d = [{'x': 1, 'y': 2}, {'x': 1, 'z': 3}, {'y': 2, 'z': 3}]
# print(task_func(d))
import unittest
class TestCases(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(task_func([]), {'x': Counter(), 'y': Counter(), 'z': Counter()})
    def test_all_keys_present(self):
        data = [{'x': 1, 'y': 2, 'z': 3}, {'x': 1, 'y': 3, 'z': 2}]
        expected = {'x': Counter({1: 2}), 'y': Counter({2: 1, 3: 1}), 'z': Counter({3: 1, 2: 1})}
        self.assertEqual(task_func(data), expected)
    def test_missing_keys(self):
        data = [{'x': 1}, {'y': 2}, {'z': 3}]
        expected = {'x': Counter({1: 1}), 'y': Counter({2: 1}), 'z': Counter({3: 1})}
        self.assertEqual(task_func(data), expected)
    def test_duplicate_values(self):
        data = [{'x': 1, 'y': 2, 'z': 3}, {'x': 1, 'y': 2, 'z': 3}, {'x': 1, 'y': 2}]
        expected = {'x': Counter({1: 3}), 'y': Counter({2: 3}), 'z': Counter({3: 2})}
        self.assertEqual(task_func(data), expected)
    def test_mixed_data_types(self):
        data = [{'x': 1, 'y': 'a', 'z': 3.5}, {'x': '1', 'y': 'a', 'z': 3.5}]
        expected = {'x': Counter({1: 1, '1': 1}), 'y': Counter({'a': 2}), 'z': Counter({3.5: 2})}
        self.assertEqual(task_func(data), expected)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)