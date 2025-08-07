import re
import pandas as pd

STOPWORDS = ["Those", "are", "the", "words", "to", "ignore"]

def task_func(text):
    # Split the text into sentences using regex to handle periods followed by spaces or end of string
    sentences = re.split(r'(?<=[.!?]) +', text.strip())
    
    # Initialize a dictionary to store sentences and their word counts
    sentence_dict = {}
    
    # Iterate over the sentences
    for i, sentence in enumerate(sentences, start=1):
        # Remove punctuation and split the sentence into words
        words = re.findall(r'\b\w+\b', sentence)
        
        # Filter out stopwords and count the remaining words
        word_count = sum(1 for word in words if word not in STOPWORDS)
        
        # Only add non-empty sentences to the dictionary
        if word_count > 0:
            sentence_dict[f"Sentence {i}"] = word_count
    
    # Create a pandas Series from the dictionary
    sentence_series = pd.Series(sentence_dict)
    
    return sentence_series

# Example usage:
# text = "Those are the words to ignore. This is a test sentence. Another sentence here."
# print(task_func(text))
import unittest
class TestCases(unittest.TestCase):
    """Test cases for the task_func function."""
    def test_case_1(self):
        text = "This is a sample sentence. This sentence contains sample words."
        expected_output = pd.Series({"Sentence 1": 5, "Sentence 2": 4})
        result = task_func(text)
        pd.testing.assert_series_equal(result, expected_output)
    def test_case_2(self):
        text = "Hello. My name is Marc. I'm here to help. How can I assist you today?"
        expected_output = pd.Series(
            {"Sentence 1": 1, "Sentence 2": 4, "Sentence 3": 3, "Sentence 4": 6}
        )
        result = task_func(text)
        pd.testing.assert_series_equal(result, expected_output)
    def test_case_3(self):
        text = "This is a test. Stopwords are words which do not contain important meaning."
        expected_output = pd.Series({"Sentence 1": 4, "Sentence 2": 7})
        result = task_func(text)
        pd.testing.assert_series_equal(result, expected_output)
    def test_case_4(self):
        text = "Hello! How are you? I'm fine, thanks."
        expected_output = pd.Series(
            {"Sentence 1": 6}
        )  # Only the last sentence is split by a period
        result = task_func(text)
        pd.testing.assert_series_equal(result, expected_output)
    def test_case_5(self):
        text = ""
        expected_output = pd.Series()
        result = task_func(text)
        pd.testing.assert_series_equal(result, expected_output)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)