import string
import random
from collections import Counter

def task_func(n, seed=None):
    # Set the seed for consistent randomness if provided
    if seed is not None:
        random.seed(seed)
    
    # Generate a list of random lowercase letters
    letters = [random.choice(string.ascii_lowercase) for _ in range(n)]
    
    # Count the occurrences of each letter using Counter
    letter_counts = Counter(letters)
    
    return letter_counts

# Example usage:
# result = task_func(100, seed=42)
# print(result)
import unittest
from collections import Counter
class TestCases(unittest.TestCase):
    def test_randomness_with_seed(self):
        # Using a seed should give consistent results
        result1 = task_func(100, seed=1)
        result2 = task_func(100, seed=1)
        self.assertEqual(result1, result2)
    def test_randomness_without_seed(self):
        # Without a seed, the results should be potentially different
        result1 = task_func(100)
        result2 = task_func(100)
        self.assertNotEqual(result1, result2)
    def test_validity_of_counts(self):
        # The total counts should equal the number of letters generated
        num_letters = 200
        result = task_func(num_letters, seed=2)
        self.assertEqual(sum(result.values()), num_letters)
    def test_non_negative_counts(self):
        # All counts should be non-negative
        result = task_func(100, seed=3)
        self.assertTrue(all(count >= 0 for count in result.values()))
    def test_type_of_return_value(self):
        # The return type should be a Counter object
        result = task_func(100, seed=4)
        self.assertIsInstance(result, Counter)
    def test_return_value(self):
        # test specific values
        result = task_func(10, seed=42)
        exp = Counter({'d': 2, 'x': 2, 'h': 2, 'u': 1, 'a': 1, 'i': 1, 'e': 1})
        self.assertEqual(result, exp)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)