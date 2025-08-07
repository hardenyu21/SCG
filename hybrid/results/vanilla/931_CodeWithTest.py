from collections import defaultdict
import re

def task_func(word: str) -> dict:
    # Sanitize the word to include only alphabetic characters
    sanitized_word = re.sub(r'[^a-zA-Z]', '', word)
    
    # Initialize a defaultdict to store two-letter combinations and their counts
    two_letter_counts = defaultdict(int)
    
    # Iterate over the sanitized word to find two-letter combinations
    for i in range(len(sanitized_word) - 1):
        # Extract the two-letter combination
        two_letter_combination = sanitized_word[i:i+2]
        # Increment the count for this combination
        two_letter_counts[two_letter_combination] += 1
    
    return two_letter_counts
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        result = task_func('abcdef')
        expected = {'ab': 1, 'bc': 1, 'cd': 1, 'de': 1, 'ef': 1}
        self.assertEqual(result, expected)
    def test_case_2(self):
        result = task_func('aabbcc')
        expected = {'aa': 1, 'ab': 1, 'bb': 1, 'bc': 1, 'cc': 1}
        self.assertEqual(result, expected)
    def test_case_3(self):
        result = task_func('a')
        expected = {}
        self.assertEqual(result, expected)
    def test_case_4(self):
        result = task_func('')
        expected = {}
        self.assertEqual(result, expected)
    def test_case_5(self):
        result = task_func('AbCd')
        expected = {'Ab': 1, 'bC': 1, 'Cd': 1}
        self.assertEqual(result, expected)
    def test_case_6(self):
        # Test with non-alphabetic characters in the word
        result = task_func('a1!b@c#d$')
        expected = {'ab': 1, 'bc': 1, 'cd': 1}
        self.assertEqual(result, expected)
    def test_case_7(self):
        # Test with mixed case and non-alphabetic characters
        result = task_func('AaBb!!Cc123')
        expected = {'Aa': 1, 'aB': 1, 'Bb': 1, 'bC': 1, 'Cc': 1}
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)