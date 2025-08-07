import itertools
import math

def task_func(x):
    # Generate all possible pairs of keys
    key_pairs = list(itertools.combinations(x.keys(), 2))
    
    # Initialize variables to track the best pair and its cosine sum
    max_cosine_sum = -float('inf')
    best_pair = None
    
    # Iterate over each key pair
    for key1, key2 in key_pairs:
        # Calculate the cosine of each value
        cos_value1 = math.cos(x[key1])
        cos_value2 = math.cos(x[key2])
        
        # Calculate the sum of the cosines
        cosine_sum = cos_value1 + cos_value2
        
        # Update the best pair if this sum is higher
        if cosine_sum > max_cosine_sum:
            max_cosine_sum = cosine_sum
            best_pair = (key1, key2)
    
    return best_pair

# Example usage:
# x = {'a': 0, 'b': math.pi/2, 'c': math.pi}
# print(task_func(x))  # Output should be a pair of keys with the highest cosine sum
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(sorted(task_func({'a': 1, 'b': 2, 'c': 3})), sorted(('a', 'b')))
    
    def test_case_2(self):
        self.assertEqual(sorted(task_func({'a': 1, 'b': 2, 'c': 3, 'd': 4})), sorted(('a', 'b')))
    def test_case_3(self):
        self.assertEqual( sorted(task_func({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})),  sorted(('e', 'a')))
    def test_case_4(self):
        self.assertEqual( sorted(task_func({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6})),  sorted(('f', 'a')))
    def test_case_5(self):
        self.assertEqual( sorted(task_func({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7})),  sorted(('g', 'f')))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)