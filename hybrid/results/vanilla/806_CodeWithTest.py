import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from collections import Counter

# Constants
STOPWORDS = set(stopwords.words('english'))

def task_func(text, n=2):
    # Remove punctuation and convert to lowercase
    text = re.sub(r'[^\w\s]', '', text).lower()
    
    # Split text into words
    words = text.split()
    
    # Remove duplicates and stopwords
    unique_words = []
    seen = set()
    for word in words:
        if word not in STOPWORDS and word not in seen:
            unique_words.append(word)
            seen.add(word)
    
    # Generate n-grams
    ngrams = zip(*[unique_words[i:] for i in range(n)])
    
    # Count n-grams
    ngram_counts = Counter(ngrams)
    
    return dict(ngram_counts)

# Example usage:
# text = "This is a sample text with some sample words and some sample text."
# print(task_func(text))
import unittest
from collections import Counter
import string
class TestCases(unittest.TestCase):
    def test_case_1(self):
        """
        Test Case 1: Simple Text
        - Input: A simple text string with no duplicated words or stopwords
        - Expected Output: A Counter object with the count of each bigram
        """
        text = "The quick brown fox jumps over the lazy dog."
        result = task_func(text)
        expected = Counter({('quick', 'brown'): 1, ('brown', 'fox'): 1, ('fox', 'jumps'): 1, ('jumps', 'lazy'): 1, ('lazy', 'dog'): 1})
        self.assertEqual(result, expected)
    def test_case_2(self):
        """
        Test Case 2: Text with Duplicated Words
        - Input: A text string with duplicated consecutive words
        - Expected Output: A Counter object with the count of each bigram, excluding duplicated words
        """
        text = "This is is a simple simple test test."
        result = task_func(text)
        expected = Counter({('simple', 'simple'): 1, ('simple', 'test'): 1, ('test', 'test'): 1})
        self.assertEqual(result, expected)
    def test_case_3(self):
        """
        Test Case 3: Text with Stopwords
        - Input: A text string with common English stopwords
        - Expected Output: A Counter object with the count of each bigram, excluding stopwords
        """
        text = "This is a test of the function."
        result = task_func(text)
        expected = Counter({('test', 'function'): 1})
        self.assertEqual(result, expected)
    def test_case_4(self):
        # This test involves punctuation; ensure punctuation handling is consistent with function logic
        text = "Hello, world!"
        result = task_func(text)
        expected = Counter({
            ('hello', 'world'): 1
        })
        self.assertEqual(result, expected)
    def test_case_5(self):
        """
        Test Case 5: Empty Text
        - Input: An empty text string
        - Expected Output: An empty Counter object
        """
        text = ""
        result = task_func(text)
        expected = Counter()
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)