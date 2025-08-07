import re
from nltk.corpus import words
import nltk

# Ensure the words corpus is downloaded
nltk.download('words')

# Constants
SAMPLE_ENGLISH_WORDS = set(words.words())  # Correct initialization

def task_func(s, n):
    # Convert the string to lowercase to ensure case insensitivity
    s = s.lower()
    
    # Use regex to find all words in the string
    words_in_string = re.findall(r'\b\w+\b', s)
    
    # Filter out only the English words
    english_words = {word for word in words_in_string if word in SAMPLE_ENGLISH_WORDS}
    
    # Return up to n different English words
    return list(english_words)[:n]

# Example usage:
# result = task_func("Hello world! This is a test string with some English words.", 5)
# print(result)
import unittest
class TestCases(unittest.TestCase):
    def setUp(self):
        random.seed(0)
    
    def test_extract_english_words(self):
        s = "This is a test string with some random words: apple, banana, test, hello, world"
        result = task_func(s, 5)
        self.assertTrue(all(word in SAMPLE_ENGLISH_WORDS for word in result))
        self.assertEqual(len(result), 5)
        self.assertEqual(len(set(result)), len(result), "All words should be unique")
    def test_fewer_than_n_words(self):
        s = "hello world"
        result = task_func(s, 5)
        self.assertTrue(len(result) <= 5)
        self.assertTrue(all(word in SAMPLE_ENGLISH_WORDS for word in result))
    def test_no_english_words(self):
        s = "xyz abcdef"
        result = task_func(s, 5)
        self.assertEqual(len(result), 0)
    def test_case_insensitivity(self):
        s = "Apple BANANA Test"
        result = task_func(s, 3)
        self.assertTrue(all(word.lower() in SAMPLE_ENGLISH_WORDS for word in result))
        self.assertEqual(len(result), 3)
    def test_duplicate_words(self):
        s = "apple banana apple banana"
        result = task_func(s, 5)
        self.assertTrue(all(word in SAMPLE_ENGLISH_WORDS for word in result))
        self.assertEqual(len(result), 4)
        self.assertEqual(set(result), {"apple", "banana"})


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)