import pandas as pd
import regex as re
from sklearn.feature_extraction.text import CountVectorizer

def task_func(text):
    # Split the text into sentences using regex to handle periods followed by spaces or newlines
    sentences = re.split(r'\.\s*', text)
    
    # Filter out empty sentences
    sentences = [sentence for sentence in sentences if sentence.strip()]
    
    # Initialize the CountVectorizer
    vectorizer = CountVectorizer()
    
    # Fit and transform the sentences to create the document-term matrix
    dtm = vectorizer.fit_transform(sentences)
    
    # Create a DataFrame from the document-term matrix
    df_dtm = pd.DataFrame(dtm.toarray(), columns=vectorizer.get_feature_names_out())
    
    return df_dtm
import unittest
class TestCases(unittest.TestCase):
    """Test cases for the task_func function."""
    def test_case_1(self):
        # Test with a basic input
        text = "This is a sample sentence. This sentence contains sample words."
        dtm = task_func(text)
        # Assertions
        self.assertEqual(
            dtm.shape, (2, 6)
        )  # Expected 2 rows (sentences) and 6 unique words
        self.assertEqual(dtm["sample"].tolist(), [1, 1])
        self.assertEqual(dtm["this"].tolist(), [1, 1])
    def test_case_2(self):
        # Test with a single sentence (with a trailing period)
        text = "A single sentence."
        dtm = task_func(text)
        # Assertions
        self.assertEqual(
            dtm.shape, (1, 2)
        )  # Expected 1 rows (sentences) and 2 unique words
        self.assertEqual(dtm["single"].tolist(), [1])
    def test_case_3(self):
        # Test with no periods (still should consider it as one sentence)
        text = "No periods in this text"
        dtm = task_func(text)
        # Assertions
        self.assertEqual(
            dtm.shape, (1, 5)
        )  # Expected 1 row (sentence) and 5 unique words
        self.assertEqual(dtm["text"].tolist(), [1])
    def test_case_4(self):
        # Test with a single sentence (with same word multiple times)
        text = ("test test test test test test test test test test test " * 3).strip()
        dtm = task_func(text)
        # Assertions
        self.assertEqual(
            dtm.shape, (1, 1)
        )  # Expected 1 row (sentence) and 1 unique words
        self.assertEqual(dtm["test"].tolist(), [33])
    def test_case_5(self):
        # Test with no periods (still should consider it as one sentence)
        text = "This is the first sentence. This is the second sentence. This is the third sentence. This is the fourth sentence. This is the fith and last sentence."
        dtm = task_func(text)
        # Assertions
        self.assertEqual(
            dtm.shape, (5, 11)
        )  # Expected 5 rows (sentence) and 11 unique words
        self.assertEqual(dtm["this"].tolist(), [1, 1, 1, 1, 1])
        self.assertEqual(dtm["is"].tolist(), [1, 1, 1, 1, 1])
        self.assertEqual(dtm["the"].tolist(), [1, 1, 1, 1, 1])
        self.assertEqual(dtm["sentence"].tolist(), [1, 1, 1, 1, 1])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)