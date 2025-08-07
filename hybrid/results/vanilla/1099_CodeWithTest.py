import re
from collections import Counter

# Predefined list of common stopwords
PREDEFINED_STOPWORDS = {
    "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", 
    "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", 
    "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", 
    "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", 
    "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", 
    "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", 
    "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", 
    "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", 
    "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "more"
}

def task_func(text):
    # Remove URLs starting with http or https
    text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)
    
    # Split the text into words
    words = text.split()
    
    # Filter out stopwords
    stopwords = [word for word in words if word.lower() in PREDEFINED_STOPWORDS]
    
    # Count the frequency of each stopword
    stopword_counts = Counter(stopwords)
    
    # Convert the Counter object to a list of tuples
    result = list(stopword_counts.items())
    
    return result
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test with a URL
        input_text = 'Visit https://www.python.org for more info. Python is great.'
        expected_output = [('for', 1), ('more', 1), ('is', 1)]
        self.assertEqual(task_func(input_text), expected_output)
    def test_case_2(self):
        # Test without a URL
        input_text = 'Python is an amazing programming language.'
        expected_output = [('is', 1), ('an', 1)]
        self.assertEqual(task_func(input_text), expected_output)
    def test_case_3(self):
        # Test with long text
        input_text = "Python is an interpreted, high-level and general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects."
        expected_output = [('is', 1), ('an', 1), ('and', 4), ('by', 1), ('in', 1), ('with', 1), ('its', 1), ('of', 1), ('to', 1), ('for', 1)]
        print(task_func(input_text))
        self.assertEqual(task_func(input_text), expected_output)
    def test_case_4(self):
        # Test with multiple URLs
        input_text = 'Check out https://www.python.org and https://www.djangoproject.com. Both are amazing.'
        expected_output = [('out', 1), ('and', 1), ('are', 1)]
        self.assertEqual(task_func(input_text), expected_output)
    def test_case_5(self):
        # Test with short text
        input_text = 'I love Python.'
        expected_output = []
        self.assertEqual(task_func(input_text), expected_output)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)