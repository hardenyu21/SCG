import re
import string
from nltk.stem import PorterStemmer
from collections import Counter

STEMMER = PorterStemmer()

def task_func(content):
    # Remove punctuation and convert to lowercase
    content = content.translate(str.maketrans('', '', string.punctuation)).lower()
    
    # Split the content into words
    words = content.split()
    
    # Stem all words except the last one
    stemmed_words = [STEMMER.stem(word) for word in words[:-1]]
    
    # Count the frequency of each stemmed word
    frequency = Counter(stemmed_words)
    
    return dict(frequency)

# Example usage:
# print(task_func("The quick brown foxes jumped over the lazy dogs."))
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        result = task_func('running runner run')
        self.assertEqual(result, {'run': 1, 'runner': 1})
    
    def test_case_2(self):
        result = task_func('dancing dancer danced')
        self.assertEqual(result, {'danc': 1, 'dancer': 1})
        
    def test_case_3(self):
        result = task_func('loving lover love')
        self.assertEqual(result, {'love': 1, 'lover': 1})
        
    def test_case_4(self):
        result = task_func('computing computer compute')
        self.assertEqual(result, {'comput': 2})
        
    def test_case_5(self):
        result = task_func('swimming swimmer swim')
        self.assertEqual(result, {'swim': 1, 'swimmer': 1})


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)