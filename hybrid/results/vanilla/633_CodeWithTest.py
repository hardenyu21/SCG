import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

# Ensure the stopwords are downloaded
import nltk
nltk.download('stopwords')
nltk.download('punkt')

def task_func(text: str) -> dict:
    # Define a set of common English stopwords
    stop_words = set(stopwords.words('english'))
    
    # Tokenize the text into words
    words = word_tokenize(text.lower())
    
    # Remove punctuation and stopwords, and filter out duplicate words
    filtered_words = []
    seen = set()
    for word in words:
        if word.isalpha() and word not in stop_words and word not in seen:
            filtered_words.append(word)
            seen.add(word)
    
    # Create a frequency distribution of the remaining words
    frequency_distribution = Counter(filtered_words)
    
    return dict(frequency_distribution)

# Example usage
print(task_func("hello hello world"))  # Output: {'hello': 1, 'world': 1}
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        input_text = "The quick brown fox jumps over the lazy dog and the dog was not that quick to respond."
        output = task_func(input_text)
        expected_output = {'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'lazy': 1, 'dog': 1, 'respond': 1}
        self.assertEqual(output, expected_output)
    def test_case_2(self):
        input_text = "hello hello world"
        output = task_func(input_text)
        expected_output = {'hello': 1, 'world': 1}
        self.assertEqual(output, expected_output)
    def test_case_3(self):
        input_text = "the and is"
        output = task_func(input_text)
        expected_output = {}
        self.assertEqual(output, expected_output)
    def test_case_4(self):
        input_text = ""
        output = task_func(input_text)
        expected_output = {}
        self.assertEqual(output, expected_output)
    def test_case_5(self):
        input_text = "hello1 hello2 hello1"
        output = task_func(input_text)
        expected_output = {'hello1': 1, 'hello2': 1}
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)