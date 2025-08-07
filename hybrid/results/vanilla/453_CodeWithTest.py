import re
import string
from random import choice

def task_func(n, pattern):
    while True:
        # Generate a random string of length n using uppercase and lowercase letters
        random_string = ''.join(choice(string.ascii_letters) for _ in range(n))
        # Check if the generated string matches the given pattern
        if re.match(pattern, random_string):
            return random_string

# Example usage:
# This will generate a random string of length 3 that consists only of uppercase letters
print(task_func(3, '^[A-Z]+$'))
import unittest
import re
class TestCases(unittest.TestCase):
    def test_correct_length(self):
        # Ensure the generated string has the requested length
        self.assertEqual(len(task_func(5, '^[a-z]*$')), 5)
    def test_pattern_matching(self):
        # Check if the generated string matches a simple pattern
        self.assertTrue(re.match('^[a-z]+$', task_func(5, '^[a-z]+$')))
    def test_lowercase_letters(self):
        # Verify the function generates a string of only lowercase letters
        self.assertTrue(re.match('^[a-z]{10}$', task_func(10, '^[a-z]{10}$')))
    def test_uppercase_letters(self):
        # Verify the function generates a string of only uppercase letters
        self.assertTrue(re.match('^[A-Z]{10}$', task_func(10, '^[A-Z]{10}$')))
    def test_mixed_case_letters(self):
        # Ensure the function can handle mixed case patterns
        pattern = '^[A-Za-z]{10}$'
        result = task_func(10, pattern)
        self.assertTrue(re.match(pattern, result) and any(c.islower() for c in result) and any(c.isupper() for c in result))
    def test_zero_length_string(self):
        # Test for generating a zero-length string, expecting an empty string as a result
        self.assertEqual(task_func(0, '^$'), '')


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)