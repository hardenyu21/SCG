import collections
from itertools import zip_longest
from random import choices

def task_func(l1, l2, K=10):
    # Combine the two lists by alternating their elements
    combined_list = [item for pair in zip_longest(l1, l2) for item in pair if item is not None]
    
    # Create a random sample of size K from the combined list
    sample = choices(combined_list, k=K)
    
    # Calculate the frequency of each element in the sample
    frequency_counter = collections.Counter(sample)
    
    return frequency_counter

# Example usage:
# l1 = [1, 2, 3]
# l2 = ['a', 'b', 'c', 'd', 'e']
# K = 10
# print(task_func(l1, l2, K))
import unittest
import collections
import random
class TestCases(unittest.TestCase):
    def setUp(self):
    # Set a consistent random seed for predictable outcomes in all tests.
        random.seed(42)
    def test_case_1(self):
        # Verify that combining two equal-length lists produces a correctly sized sample.
        l1 = list(range(10))
        l2 = list(range(10, 20))
        freq = task_func(l1, l2)
        self.assertIsInstance(freq, collections.Counter)
        self.assertEqual(sum(freq.values()), 10)
    def test_case_2(self):
        # Test combining two short, equal-length lists to ensure correct sample size.
        l1 = list(range(5))
        l2 = list(range(10, 15))
        freq = task_func(l1, l2)
        self.assertIsInstance(freq, collections.Counter)
        self.assertEqual(sum(freq.values()), 10)
    def test_case_3(self):
        # Check correct sampling from two equal-length lists starting from different ranges.
        l1 = list(range(20, 30))
        l2 = list(range(30, 40))
        freq = task_func(l1, l2)
        self.assertIsInstance(freq, collections.Counter)
        self.assertEqual(sum(freq.values()), 10)
    def test_case_4(self):
        # Ensure that combining two long, equal-length lists correctly manages the sample size.
        l1 = list(range(50))
        l2 = list(range(50, 100))
        freq = task_func(l1, l2)
        self.assertIsInstance(freq, collections.Counter)
        self.assertEqual(sum(freq.values()), 10)
    def test_case_5(self):
        # Confirm that an empty first list results in sampling exclusively from the second list.
        l1 = []
        l2 = list(range(10, 20))
        freq = task_func(l1, l2)
        self.assertIsInstance(freq, collections.Counter)
        self.assertEqual(sum(freq.values()), 10)
    def test_case_with_non_integers(self):
        # Check sampling behavior with lists of non-integer floating-point numbers.
        l1 = [0.1, 0.2, 0.3]
        l2 = [0.4, 0.5, 0.6]
        freq = task_func(l1, l2)
        self.assertIsInstance(freq, collections.Counter)
        self.assertEqual(sum(freq.values()), 10)
        most_common = freq.most_common(1)[0][0]
        self.assertIn(most_common, [0.1, 0.2, 0.3, 0.4, 0.5, 0.6])
    def test_imbalanced_lists(self):
        # Test sampling from two lists where one is significantly longer to ensure fair representation.
        l1 = [1, 2, 3]
        l2 = list(range(4, 104))
        freq = task_func(l1, l2)
        self.assertIsInstance(freq, collections.Counter)
        self.assertEqual(sum(freq.values()), 10)
        self.assertTrue(any(item in freq for item in l1))
    def test_empty_first_list(self):
        # Verify behavior and sampling correctness when the first list is empty.
        l1 = []
        l2 = list(range(10, 20))
        freq = task_func(l1, l2)
        self.assertIsInstance(freq, collections.Counter)
        self.assertEqual(sum(freq.values()), 10)
        self.assertTrue(all(item in l2 for item in freq.elements()))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)