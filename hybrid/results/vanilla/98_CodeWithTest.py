import random
import string
from collections import Counter

def task_func(num_strings, string_length):
    # Generate a list of random strings
    random_strings = [''.join(random.choices(string.ascii_lowercase, k=string_length)) for _ in range(num_strings)]
    
    # Concatenate all strings into a single string
    all_characters = ''.join(random_strings)
    
    # Count the frequency of each character
    character_counts = Counter(all_characters)
    
    # Sort characters by frequency in descending order
    sorted_characters = sorted(character_counts.items(), key=lambda item: item[1], reverse=True)
    
    return sorted_characters

# Example usage:
# result = task_func(10, 5)
# print(result)
import unittest
import random
class TestCases(unittest.TestCase):
    def setUp(self):
        # This method will be run before each test.
        random.seed(0)  # Set a seed for reproducibility in all tests
    def test_return_type(self):
        """ Test that the function returns a list. """
        result = task_func(100, 5)
        self.assertIsInstance(result, list)
    def test_list_length(self):
        """ Test that the length of the list is not greater than the number of unique characters. """
        result = task_func(100, 5)
        self.assertLessEqual(len(result), 26)  # 26 letters in the ASCII lowercase alphabet
    def test_tuple_structure(self):
        """ Test that each element in the list is a tuple with two elements. """
        result = task_func(100, 5)
        for item in result:
            self.assertIsInstance(item, tuple)
            self.assertEqual(len(item), 2)
    def test_deterministic_output(self):
        """ Test the function with a predefined seed for reproducibility. """
        result = task_func(100, 5)
        self.assertTrue(all(isinstance(pair, tuple) and len(pair) == 2 for pair in result))
        self.assertGreater(len(result), 0)  # Ensure the result is not empty
    def test_specific_character_count(self):
        """ Test if a specific character count is as expected based on the seed. """
        result = task_func(100, 5)
        specific_char = 'a'  # Example character to check
        specific_count = next((count for char, count in result if char == specific_char), 0)
        self.assertGreater(specific_count, 0)  # Check if the count for the specific character is greater than 0
    def test_zero_strings(self):
        """ Test the function returns an empty list when no strings are generated. """
        result = task_func(0, 5)
        self.assertEqual(result, [])
    def test_zero_length(self):
        """ Test the function with string_length of zero returns empty strings but counts them. """
        result = task_func(100, 0)
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)