from string import ascii_lowercase
import re
from collections import Counter

# Constants
LETTERS_PATTERN = re.compile(r'^(.*?)-[a-z]$')
LETTERS = ascii_lowercase

def task_func(string):
    # Find the last occurrence of "-" and split the string
    match = LETTERS_PATTERN.search(string)
    if match:
        prefix = match.group(1)
    else:
        # If no "-" is found, consider the whole string as the prefix
        prefix = string

    # Count the frequency of each lowercase letter in the prefix
    frequency = Counter(char for char in prefix if char in LETTERS)

    return dict(frequency)

# Example usage:
# print(task_func("hello-world-a"))  # Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
# print(task_func("example"))        # Output: {'e': 2, 'x': 1, 'a': 1, 'm': 1, 'p': 1, 'l': 1}
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        result = task_func('abc-def-ghij')
        expected = {letter: 1 if letter in 'abcdef' else 0 for letter in ascii_lowercase}
        self.assertEqual(result, expected)
    def test_case_2(self):
        result = task_func('abcdefghij')
        expected = {letter: 1 if letter in 'abcdefghij' else 0 for letter in ascii_lowercase}
        self.assertEqual(result, expected)
    def test_case_3(self):
        result = task_func('aabbcc-def')
        expected = {letter: 2 if letter in 'aabbcc' else 0 for letter in ascii_lowercase}
        self.assertEqual(result, expected)
    def test_case_4(self):
        result = task_func('')
        expected = {letter: 0 for letter in ascii_lowercase}
        self.assertEqual(result, expected)
    def test_case_5(self):
        result = task_func('xyz-abc')
        expected = {letter: 1 if letter in 'xyz' else 0 for letter in ascii_lowercase}
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)