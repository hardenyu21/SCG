import re
from nltk.stem import PorterStemmer
import pandas as pd

def task_func(text_series):
    # Initialize the PorterStemmer
    stemmer = PorterStemmer()
    
    # Define a function to process each text
    def process_text(text):
        # Convert to lowercase
        text = text.lower()
        # Remove non-alphanumeric characters except spaces
        text = re.sub(r'[^a-z0-9\s]', '', text)
        # Split the text into words
        words = text.split()
        # Stem each word
        stemmed_words = [stemmer.stem(word) for word in words]
        # Join the stemmed words back into a single string
        return ' '.join(stemmed_words)
    
    # Apply the process_text function to each element in the Series
    processed_series = text_series.apply(process_text)
    
    return processed_series

# Example usage:
# text_series = pd.Series(["Hello, World!", "Pandas are great!"])
# processed_series = task_func(text_series)
# print(processed_series)
import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    
    def test_lowercase_and_stemming(self):
        """
        Test case to ensure that all text is converted to lowercase and words are stemmed properly.
        """
        input_series = pd.Series(["THIS IS A TEST.", "Test, case number 2!"])
        expected_output = pd.Series(["thi is a test", "test case number 2"])
        processed_series = task_func(input_series)
        pd.testing.assert_series_equal(processed_series, expected_output)
    def test_numerics_and_special_characters(self):
        """
        Test case to verify that numeric characters are retained and special characters are removed.
        """
        input_series = pd.Series(["Another Test 123.", "456 Anoth3r one!"])
        expected_output = pd.Series(["anoth test 123", "456 anoth3r one"])
        processed_series = task_func(input_series)
        pd.testing.assert_series_equal(processed_series, expected_output)
    def test_empty_strings(self):
        """
        Test case to check the function's handling of empty strings.
        """
        input_series = pd.Series(["", " "])
        expected_output = pd.Series(["", ""])
        processed_series = task_func(input_series)
        pd.testing.assert_series_equal(processed_series, expected_output)
    def test_punctuation(self):
        """
        Test case to check that punctuation is removed from the text.
        """
        input_series = pd.Series(["Punctuation! Should, be: removed; right?"])
        expected_output = pd.Series(["punctuat should be remov right"])
        processed_series = task_func(input_series)
        pd.testing.assert_series_equal(processed_series, expected_output)
    def test_stemconsistency(self):
        """
        Test case to ensure that stemming is consistent across different forms of words.
        """
        input_series = pd.Series(["Stemming should work on words like running", "stemmed works on stemmed"])
        expected_output = pd.Series(["stem should work on word like run", "stem work on stem"])
        processed_series = task_func(input_series)
        pd.testing.assert_series_equal(processed_series, expected_output)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)