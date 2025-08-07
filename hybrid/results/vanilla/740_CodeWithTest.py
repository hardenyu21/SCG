from collections import Counter
import heapq
import random

# Constants
LETTERS = list('abcdefghijklmnopqrstuvwxyz')

def task_func(my_dict):
    # Count the occurrences of each letter in the dictionary
    letter_counts = Counter(my_dict.keys())
    
    # Find the 3 most common letters using a heap
    most_common_letters = heapq.nlargest(3, letter_counts, key=letter_counts.get)
    
    return most_common_letters

# Example usage
if __name__ == "__main__":
    # Create a dictionary with random integers as values
    my_dict = {letter: random.randint(1, 100) for letter in LETTERS}
    
    # Get the 3 most common letters
    result = task_func(my_dict)
    print("The 3 most common letters are:", result)
import unittest
import random
LETTERS = list('abcdefghijklmnopqrstuvwxyz')
def generate_random_dict(size=26, min_val=1, max_val=100):
    """Generate a random dictionary with letters as keys and random integers as values."""
    letters = random.sample(LETTERS, size)
    return {letter: random.randint(min_val, max_val) for letter in letters}
class TestCases(unittest.TestCase):
    def test_basic(self):
        # Basic Test
        test_dict = generate_random_dict()
        result = task_func(test_dict)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 3)
        self.assertTrue(all(isinstance(letter, str) for letter in result))
    def test_few_letters(self):
        # Edge Case: Fewer than 3 letters
        test_dict = {'a': 10, 'b': 20}
        result = task_func(test_dict)
        self.assertEqual(result, ['b', 'a'])
    def test_empty_dict(self):
        # Edge Case: Empty dictionary
        test_dict = {}
        result = task_func(test_dict)
        self.assertEqual(result, [])
    def test_specific_letters(self):
        # Specific Test: Known output
        test_dict = {'a': 100, 'b': 90, 'c': 80, 'd': 70}
        result = task_func(test_dict)
        self.assertEqual(result, ['a', 'b', 'c'])
    def test_general(self):
        # General Test: Check top 3 values
        test_dict = generate_random_dict()
        result = task_func(test_dict)
        sorted_values = sorted(test_dict.values(), reverse=True)[:3]
        sorted_keys = [k for k, v in sorted(test_dict.items(), key=lambda item: item[1], reverse=True)][:3]
        self.assertEqual(result, sorted_keys)
        self.assertEqual([test_dict[key] for key in result], sorted_values)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)