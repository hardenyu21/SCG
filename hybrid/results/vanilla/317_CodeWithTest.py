import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import re

def task_func(example_str):
    # Extract text not enclosed in square brackets
    extracted_text = re.sub(r'\[.*?\]', '', example_str)
    
    # Split the text into words
    words = extracted_text.split()
    
    # Create a TF-IDF vectorizer
    vectorizer = TfidfVectorizer()
    
    # Fit and transform the words into a TF-IDF matrix
    tfidf_matrix = vectorizer.fit_transform([' '.join(words)])
    
    # Get feature names (words)
    feature_names = vectorizer.get_feature_names_out()
    
    # Get the TF-IDF scores
    tfidf_scores = tfidf_matrix.toarray()[0]
    
    # Create a dictionary with words as keys and TF-IDF scores as values
    tfidf_dict = {word: score for word, score in zip(feature_names, tfidf_scores)}
    
    return tfidf_dict

# Example usage:
example_str = "This is a sample text [with some text in brackets] and more text."
print(task_func(example_str))
import unittest
import doctest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        input_str = "Adversarial ] input ][[][ i[s []] a [ problem ] in [ machine learning ]"
        output = task_func(input_str)
        expected_output = {
            'adversarial': 0.5773502691896258, 
            'in': 0.5773502691896258, 
            'input': 0.5773502691896258
        }
        self.assertDictEqual(output, expected_output)
    def test_case_2(self):
        input_str = "Alice [1234 Street, City, State] Bob Charlie [5678 Street, AnotherCity, State]"
        output = task_func(input_str)
        expected_output = {
            'alice': 0.5773502691896258, 
            'bob': 0.5773502691896258, 
            'charlie': 0.5773502691896258
        }
        self.assertDictEqual(output, expected_output)
    def test_case_3(self):
        input_str = "No brackets here at all"
        output = task_func(input_str)
        expected_output = {
            'all': 0.4472135954999579, 
            'at': 0.4472135954999579, 
            'brackets': 0.4472135954999579, 
            'here': 0.4472135954999579, 
            'no': 0.4472135954999579
        }
        self.assertDictEqual(output, expected_output)
    def test_case_4(self):
        input_str = "Mix [bracketed content] (and non-bracketed) content"
        output = task_func(input_str)
        expected_output = {
            'and': 0.4472135954999579, 
            'bracketed': 0.4472135954999579, 
            'content': 0.4472135954999579, 
            'mix': 0.4472135954999579, 
            'non': 0.4472135954999579
        }
        self.assertDictEqual(output, expected_output)
    def test_case_5(self):
        input_str = "[Only bracketed content]"
        output = task_func(input_str)
        expected_output = {}
        self.assertDictEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)