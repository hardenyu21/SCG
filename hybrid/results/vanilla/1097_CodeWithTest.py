import re
from string import punctuation

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
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', punctuation))
    
    # Convert text to lowercase
    text = text.lower()
    
    # Remove stopwords
    words = text.split()
    words = [word for word in words if word not in PREDEFINED_STOPWORDS]
    
    # Join the words back into a single string
    cleaned_text = ' '.join(words)
    
    return cleaned_text
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        input_text = 'Visit https://www.python.org for more info. I love to eat apples and oranges!'
        expected_output = 'Visit info love eat apples oranges'
        result = task_func(input_text)
        self.assertEqual(result, expected_output)
    def test_case_2(self):
        input_text = 'Check out https://www.google.com and also https://www.openai.com'
        expected_output = 'Check also'
        result = task_func(input_text)
        self.assertEqual(result, expected_output)
    def test_case_3(self):
        input_text = 'Hello, world! How are you today?'
        expected_output = 'Hello world How today'
        result = task_func(input_text)
        self.assertEqual(result, expected_output)
    def test_case_4(self):
        input_text = 'Machine learning AI'
        expected_output = 'Machine learning AI'
        result = task_func(input_text)
        self.assertEqual(result, expected_output)
    def test_case_5(self):
        input_text = ''
        expected_output = ''
        result = task_func(input_text)
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)