import re
import random
import string

def task_func(n, pattern, seed=None):
    # Set the seed for reproducibility
    if seed is not None:
        random.seed(seed)
    
    # Generate a random string of length 'n' using ASCII letters and digits
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=n))
    
    # Find all non-overlapping matches of the regex pattern
    matches = re.findall(pattern, random_string)
    
    return matches

# Example usage
print(task_func(1000, r'[1-9]{2}', seed=1))
import unittest
class TestCases(unittest.TestCase):
    
    def test_valid_pattern_matching(self):
        test_length = 100
        test_pattern = r'[A-Za-z]{5}'
        test_seed = 12345  # using a seed for consistency
        expected_matches = [
            'mrKBk',
            'BqJOl',
            'NJlwV',
            'UfHVA',
            'LGkjn',
            'vubDv',
            'GSVAa',
            'kXLls',
            'RKlVy',
            'vZcoh',
            'FnVZW',
            'JQlqL'
        ]
        actual_matches = task_func(test_length, test_pattern, seed=test_seed)
        self.assertEqual(actual_matches, expected_matches)
    def test_no_matches_found(self):
        test_length = 100
        test_pattern = r'XYZ'
        test_seed = 12345
        expected_matches = []
        actual_matches = task_func(test_length, test_pattern, seed=test_seed)
        self.assertEqual(actual_matches, expected_matches)
    def test_zero_length_string(self):
        test_length = 0
        test_pattern = r'[A-Za-z0-9]{5}'
        expected_matches = []
        actual_matches = task_func(test_length, test_pattern, seed=None)
        self.assertEqual(actual_matches, expected_matches)
    def test_unusual_pattern(self):
        test_length = 100
        test_pattern = r'[^A-Za-z0-9]+'
        test_seed = 67890
        expected_matches = []
        actual_matches = task_func(test_length, test_pattern, seed=test_seed)
        self.assertEqual(actual_matches, expected_matches)
    def test_extreme_input_values(self):
        test_length = 10000  # Reduced size for the environment's stability
        test_pattern = r'[A-Za-z]{5}'
        actual_matches = task_func(test_length, test_pattern, seed=None)
        self.assertIsInstance(actual_matches, list)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)