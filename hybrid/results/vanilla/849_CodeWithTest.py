import re
from nltk.corpus import stopwords
from collections import Counter

# Ensure the stopwords are downloaded
import nltk
nltk.download('stopwords')

STOPWORDS = set(stopwords.words('english'))

def task_func(input_string):
    # Split the input string into individual lines
    lines = input_string.splitlines()
    
    # Initialize a list to hold all words
    words = []
    
    # Process each line
    for line in lines:
        # Remove non-alphanumeric characters and convert to lowercase
        cleaned_line = re.sub(r'[^a-zA-Z0-9\s]', '', line).lower()
        
        # Split the line into words
        line_words = cleaned_line.split()
        
        # Filter out stopwords
        filtered_words = [word for word in line_words if word not in STOPWORDS]
        
        # Add the filtered words to the list
        words.extend(filtered_words)
    
    # Count the frequency of each word
    word_frequencies = Counter(words)
    
    return dict(word_frequencies)

# Example usage:
# input_string = "This is a test. This test is only a test."
# print(task_func(input_string))
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        input_string = "This is line one.\nThis is line two."
        expected_output = {'This': 2, 'line': 2, 'one': 1, 'two': 1}
        self.assertEqual(task_func(input_string), expected_output)
    def test_case_2(self):
        input_string = "apple orange apple\norange apple\napple"
        expected_output = {'apple': 4, 'orange': 2}
        self.assertEqual(task_func(input_string), expected_output)
    def test_case_3(self):
        input_string = "This\nThis\nThis"
        expected_output = {'This': 3}
        self.assertEqual(task_func(input_string), expected_output)
    def test_case_4(self):
        input_string = "This is a test.\nThis is only a test."
        expected_output = {'This': 2, 'test': 2}
        self.assertEqual(task_func(input_string), expected_output)
    def test_case_5(self):
        input_string = "Stop this\nStop"
        expected_output = {'Stop': 2}
        self.assertEqual(task_func(input_string), expected_output)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)