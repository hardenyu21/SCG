import random
import string
import collections

# Constants
VALID_CHARACTERS = string.ascii_letters + string.digits

def task_func(n_strings, string_length):
    # Initialize a counter to keep track of character frequencies
    char_counter = collections.Counter()
    
    # Generate n random strings
    for _ in range(n_strings):
        # Generate a random string of the specified length
        random_string = ''.join(random.choice(VALID_CHARACTERS) for _ in range(string_length))
        # Update the counter with characters from the generated string
        char_counter.update(random_string)
    
    # Convert the counter to a dictionary and return
    return dict(char_counter)

# Example usage:
# result = task_func(10, 5)
# print(result)
import unittest
from collections import Counter
class TestCases(unittest.TestCase):
    def test_single_string_single_character(self):
        # Test when n_strings=1 and string_length=1 (minimal input)
        result = task_func(1, 1)
        self.assertEqual(len(result), 1)
        self.assertEqual(sum(result.values()), 1)
    def test_multiple_strings_single_character(self):
        # Test when n_strings > 1 and string_length=1
        result = task_func(5, 1)
        self.assertTrue(len(result) <= 5)
        self.assertEqual(sum(result.values()), 5)
    def test_single_string_multiple_characters(self):
        # Test when n_strings=1 and string_length > 1
        result = task_func(1, 5)
        self.assertTrue(len(result) <= 5)
        self.assertEqual(sum(result.values()), 5)
    def test_multiple_strings_multiple_characters(self):
        # Test when n_strings > 1 and string_length > 1
        result = task_func(5, 5)
        self.assertTrue(len(result) <= 25)
        self.assertEqual(sum(result.values()), 25)
    def test_valid_characters(self):
        # Test whether the function only uses valid characters as defined in VALID_CHARACTERS
        result = task_func(100, 10)
        all_characters = ''.join(result.keys())
        self.assertTrue(all(char in VALID_CHARACTERS for char in all_characters))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)