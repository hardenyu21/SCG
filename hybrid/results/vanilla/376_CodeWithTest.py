import nltk
import re
from collections import Counter

# Ensure the stopwords are downloaded
nltk.download('stopwords')

# Constants
STOPWORDS = set(nltk.corpus.stopwords.words('english'))

def task_func(text):
    # Convert text to lowercase
    text = text.lower()
    
    # Remove punctuation using regex
    text = re.sub(r'[^\w\s]', '', text)
    
    # Split the text into words
    words = text.split()
    
    # Remove stopwords
    filtered_words = [word for word in words if word not in STOPWORDS]
    
    # Calculate the frequency of each word
    word_frequency = Counter(filtered_words)
    
    return dict(word_frequency)

# Example usage
text = "This is a sample text. This text is just a sample."
print(task_func(text))
import unittest
import doctest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Basic test
        text = 'This is a sample text. This text is for testing.'
        expected_output = {'sample': 1, 'text': 2, 'testing': 1}
        self.assertEqual(task_func(text), expected_output)
    def test_case_2(self):
        # Test with stopwords
        text = 'The quick brown fox jumped over the lazy dog.'
        expected_output = {'quick': 1, 'brown': 1, 'fox': 1, 'jumped': 1, 'lazy': 1, 'dog': 1}
        self.assertEqual(task_func(text), expected_output)
    def test_case_3(self):
        # Test with punctuation
        text = 'Hello, world! How are you today?'
        expected_output = {'hello': 1, 'world': 1, 'today': 1}
        self.assertEqual(task_func(text), expected_output)
    def test_case_4(self):
        # Test with empty string
        text = ''
        expected_output = {}
        self.assertEqual(task_func(text), expected_output)
    def test_case_5(self):
        # Test with numeric values and special characters
        text = 'Python3 is better than Python2. I love Python3.5!'
        expected_output = {'python3': 2, 'better': 1, 'python2': 1, 'love': 1, '5': 1}
        self.assertEqual(task_func(text), expected_output)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)