import re
from collections import Counter
from nltk.corpus import stopwords

def task_func(text: str) -> dict:
    # Download stopwords if not already downloaded
    try:
        stopwords.words('english')
    except LookupError:
        import nltk
        nltk.download('stopwords')
    
    # Get the set of English stopwords
    stop_words = set(stopwords.words('english'))
    
    # Use regex to find words in the text
    words = re.findall(r'\b\w+\b', text.lower())
    
    # Filter out stopwords
    non_stop_words = [word for word in words if word not in stop_words]
    
    # Count the occurrences of each non-stop word
    word_counts = Counter(non_stop_words)
    
    return dict(word_counts)

# Example usage:
# text = "This is a sample text with some sample words."
# print(task_func(text))
import unittest
import doctest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Simple sentence with some stopwords
        input_text = "This is a simple test."
        expected_output = {'simple': 1, 'test': 1}
        self.assertDictEqual(task_func(input_text), expected_output)
    def test_case_2(self):
        # Longer sentence with repeated words
        input_text = "Some words are repeated more than once. Repeated words are common."
        expected_output = {'words': 2, 'repeated': 1, 'Repeated': 1, 'common': 1}
        self.assertDictEqual(task_func(input_text), expected_output)
        
    def test_case_3(self):
        # Text with no stopwords
        input_text = "Python programming language."
        expected_output = {'Python': 1, 'programming': 1, 'language': 1}
        self.assertDictEqual(task_func(input_text), expected_output)
        
    def test_case_4(self):
        # Text with all stopwords
        input_text = "This is an and the with"
        expected_output = {}
        self.assertDictEqual(task_func(input_text), expected_output)
        
    def test_case_5(self):
        # Empty text
        input_text = ""
        expected_output = {}
        self.assertDictEqual(task_func(input_text), expected_output)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)