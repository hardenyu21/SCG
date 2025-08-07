import collections
import random

# Constants
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

def task_func(n_keys, n_values):
    # Initialize an empty dictionary
    result_dict = collections.defaultdict(list)
    
    # Generate the specified number of keys
    keys = random.sample(LETTERS, n_keys)
    
    # Assign consecutive integers to each key
    for i in range(n_values):
        key = keys[i % n_keys]  # Cycle through keys if n_values > n_keys
        result_dict[key].append(i + 1)
    
    # Convert defaultdict to a regular dict before returning
    return dict(result_dict)

# Example usage:
# print(task_func(5, 10))
import unittest
import random
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
class TestCases(unittest.TestCase):
    def test_basic_functionality(self):
        random.seed(0)
        result = task_func(3, 5)
        self.assertLessEqual(len(result), 3)
        for key in result:
            self.assertIn(key, LETTERS)
            self.assertEqual(result[key], [1, 2, 3, 4, 5])
    def test_no_keys(self):
        random.seed(0)
        result = task_func(0, 5)
        self.assertEqual(result, {})
    def test_no_values(self):
        random.seed(0)
        result = task_func(3, 0)
        for key in result:
            self.assertEqual(result[key], [])
    def test_large_input(self):
        random.seed(0)
        result = task_func(10, 1000)
        for key in result:
            self.assertIn(key, LETTERS)
            self.assertEqual(len(result[key]), 1000)
    def test_max_keys(self):
        random.seed(0)
        result = task_func(len(LETTERS), 5)
        for key in result:
            self.assertIn(key, LETTERS)
            self.assertEqual(result[key], [1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)