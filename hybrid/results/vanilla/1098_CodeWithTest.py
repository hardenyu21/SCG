import re
from collections import Counter

def task_func(text, top_n):
    # Remove URLs starting with http or https
    text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)
    
    # Tokenize the text into words
    words = re.findall(r'\b\w+\b', text.lower())
    
    # Count the frequency of each word
    word_counts = Counter(words)
    
    # Get the N most common words
    most_common_words = word_counts.most_common(top_n)
    
    return most_common_words

# Example usage:
# text = "Check out this link: https://example.com. This is a test. This test is only a test."
# top_n = 3
# print(task_func(text, top_n))
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        result = task_func('Python is great. I love Python.', 2)
        expected = [('Python', 2), ('is', 1)]
        self.assertEqual(result, expected)
    def test_case_2(self):
        result = task_func('Visit https://www.python.org for more info. Python is great. I love Python.', 2)
        expected = [('Python', 2), ('Visit', 1)]
        self.assertEqual(result, expected)
    def test_case_3(self):
        text = 'Visit https://www.python.org and http://www.example.com. Python é ótimo! Adoro Python!'
        result = task_func(text, 2)
        expected = [('Python', 2), ('Visit', 1)]
        self.assertEqual(result, expected)
    def test_case_4(self):
        result = task_func('', 2)
        expected = []
        self.assertEqual(result, expected)
    def test_case_5(self):
        result = task_func('Hello, world! How are you?', 2)
        expected = [('Hello', 1), ('world', 1)]
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)