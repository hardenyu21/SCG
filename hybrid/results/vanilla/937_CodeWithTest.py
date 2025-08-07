import re
from collections import Counter

def task_func(input_str):
    # Remove all non-alphanumeric characters and convert to lowercase
    cleaned_str = re.sub(r'[^a-zA-Z0-9]', '', input_str).lower()
    
    # Count the frequency of each character
    frequency = Counter(cleaned_str)
    
    return dict(frequency)

# Example usage:
# result = task_func("Hello, World! 123")
# print(result)  # Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1, '1': 1, '2': 1, '3': 1}
import unittest
class TestCases(unittest.TestCase):
    def test_only_letters(self):
        # Expected output adjusted for lowercase
        self.assertEqual(task_func("Hello, World!"), {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1})
    def test_empty_string(self):
        self.assertEqual(task_func(""), {})
    def test_repeated_numbers(self):
        self.assertEqual(task_func("12345 12345"), {'1': 2, '2': 2, '3': 2, '4': 2, '5': 2})
    def test_mixed_case_letters(self):
        # Expecting all lowercase after adjustment for case insensitivity
        self.assertEqual(task_func("AAaaBBbbCCcc"), {'a': 4, 'b': 4, 'c': 4})
    def test_numbers_only(self):
        self.assertEqual(task_func("111222333444555"), {'1': 3, '2': 3, '3': 3, '4': 3, '5': 3})
    def test_uppercase_only(self):
        # Expecting all lowercase after adjustment for case insensitivity
        self.assertEqual(task_func("AAAABBBBCCCC"), {'a': 4, 'b': 4, 'c': 4})
    def test_no_alphanumeric(self):
        self.assertEqual(task_func("!!!@@@###$$$%%%^^^&&&"), {})


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)