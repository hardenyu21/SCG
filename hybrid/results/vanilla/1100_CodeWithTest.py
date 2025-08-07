import re
from sklearn.feature_extraction.text import TfidfVectorizer

def task_func(texts):
    # Function to remove URLs from text
    def remove_urls(text):
        return re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)

    # Remove URLs from each document
    cleaned_texts = [remove_urls(text) for text in texts]

    # Initialize the TfidfVectorizer
    vectorizer = TfidfVectorizer()

    # Fit and transform the cleaned texts to compute TF-IDF scores
    tfidf_matrix = vectorizer.fit_transform(cleaned_texts)

    # Get the feature names (unique words)
    feature_names = vectorizer.get_feature_names_out()

    # Convert the TF-IDF matrix to a dense format and round the scores to 8 decimal places
    dense_tfidf_matrix = tfidf_matrix.todense().round(8)

    # Create a list of tuples for each document's TF-IDF scores
    tfidf_scores = [tuple(row) for row in dense_tfidf_matrix]

    # Return the result as a tuple of (list of tuples, list of str)
    return (tfidf_scores, feature_names)
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        input_texts = ['Visit https://www.python.org for more info.', 'Python is great.', 'I love Python.']
        output = task_func(input_texts)
        sorted_indices = sorted(range(len(output[1])), key=lambda k: output[1][k])
        expected_output = (
            [tuple(row[i] for i in sorted_indices) for row in output[0]],
            sorted(output[1])
        )
        self.assertEqual(output, expected_output)
    def test_case_2(self):
        input_texts = ['Hello world!', 'Python programming is fun.', 'Data science with Python.']
        output = task_func(input_texts)
        sorted_indices = sorted(range(len(output[1])), key=lambda k: output[1][k])
        expected_output = (
            [tuple(row[i] for i in sorted_indices) for row in output[0]],
            sorted(output[1])
        )
        self.assertEqual(output, expected_output)
    def test_case_3(self):
        input_texts = ['I love coding.', 'You love coding too.', 'We all love coding.']
        output = task_func(input_texts)
        sorted_indices = sorted(range(len(output[1])), key=lambda k: output[1][k])
        expected_output = (
            [tuple(row[i] for i in sorted_indices) for row in output[0]],
            sorted(output[1])
        )
        self.assertEqual(output, expected_output)
    def test_case_4(self):
        input_texts = ['Check out this amazing article at https://www.example.com/article']
        output = task_func(input_texts)
        sorted_indices = sorted(range(len(output[1])), key=lambda k: output[1][k])
        expected_output = (
            [tuple(row[i] for i in sorted_indices) for row in output[0]],
            sorted(output[1])
        )
        self.assertEqual(output, expected_output)
    def test_case_5(self):
        input_texts = ['', '', '']
        expected_output = ([], [])
        self.assertEqual(task_func(input_texts), expected_output)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)