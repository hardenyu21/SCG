from collections import Counter
import random

def task_func(length, count, seed=0):
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # Define the fixed set of letters
    letters = ['a', 'b', 'c', 'd', 'e']
    
    # Generate the specified number of random strings
    random_strings = [''.join(random.choices(letters, k=length)) for _ in range(count)]
    
    # Concatenate all strings into a single string to count letter frequencies
    all_letters = ''.join(random_strings)
    
    # Use Counter to count the frequency of each letter
    letter_frequency = Counter(all_letters)
    
    return letter_frequency

# Example usage:
# length = 5, count = 10, seed = 42
# This will generate 10 random strings of length 5 using the letters 'a', 'b', 'c', 'd', 'e'
# and return the frequency of each letter in the generated strings.
result = task_func(5, 10, 42)
print(result)
import unittest
from collections import Counter
class TestCases(unittest.TestCase):
    def test_length_one_count_ten(self):
        result = task_func(1, 10, seed=0)
        self.assertIsInstance(result, Counter)
        self.assertEqual(sum(result.values()), 10, "The total count of letters should be 10.")
        
    def test_length_five_count_hundred(self):
        result = task_func(5, 100, seed=1)
        self.assertIsInstance(result, Counter)
        self.assertEqual(sum(result.values()), 500, "The total count of letters should be 500.")
        
    def test_zero_length(self):
        result = task_func(0, 100, seed=2)
        self.assertIsInstance(result, Counter)
        self.assertEqual(sum(result.values()), 0, "With length 0, there should be no letters.")
        
    def test_zero_count(self):
        result = task_func(5, 0, seed=3)
        self.assertIsInstance(result, Counter)
        self.assertEqual(sum(result.values()), 0, "With count 0, there should be no letters.")
        
    def test_specific_distribution(self):
        # Assuming the seed value of 4 leads to a specific, known distribution
        result = task_func(5, 2, seed=4)
        # Correct the expected distribution based on actual output
        correct_expected_distribution = Counter({'b': 3, 'a': 3, 'e': 2, 'c': 1, 'd': 1})
        self.assertEqual(result, correct_expected_distribution, "The letter distribution should match the expected distribution.")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)