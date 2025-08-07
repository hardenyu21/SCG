import re
from nltk import word_tokenize
from collections import Counter

def task_func(input_str):
    # Remove all special characters, punctuation marks, and spaces
    cleaned_str = re.sub(r'[^a-zA-Z0-9\s]', '', input_str)
    
    # Tokenize the cleaned string into words
    words = word_tokenize(cleaned_str)
    
    # Count the frequency of each word
    word_freq = Counter(words)
    
    return dict(word_freq)

# Example usage:
# input_str = "Hello, world! This is a test. Hello again."
# print(task_func(input_str))
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        result = task_func('Special $#! characters   spaces 888323')
        expected = {'Special': 1, 'characters': 1, 'spaces': 1, '888323': 1}
        self.assertEqual(result, expected)
    def test_case_2(self):
        result = task_func('Hello hello world')
        expected = {'Hello': 1, 'hello': 1, 'world': 1}
        self.assertEqual(result, expected)
    def test_case_3(self):
        result = task_func('')
        expected = {}
        self.assertEqual(result, expected)
    def test_case_4(self):
        result = task_func('123 123 456')
        expected = {'123': 2, '456': 1}
        self.assertEqual(result, expected)
    def test_case_5(self):
        result = task_func('Hello123 #$! 123')
        expected = {'Hello123': 1, '123': 1}
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)