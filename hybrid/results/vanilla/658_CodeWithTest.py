import re
import nltk
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

# Make sure to download NLTK stopwords
nltk.download('stopwords')

# Define a regex pattern for matching all non-alphanumeric characters
ALPHANUMERIC = re.compile('[\W_]+')

# Load NLTK's list of English stop words
STOPWORDS = nltk.corpus.stopwords.words('english')

def task_func(texts):
    # Preprocess the text documents
    def preprocess(text):
        # Remove non-alphanumeric characters
        text = ALPHANUMERIC.sub(' ', text)
        # Convert to lowercase
        text = text.lower()
        return text

    # Preprocess all documents
    preprocessed_texts = [preprocess(text) for text in texts]

    # Initialize CountVectorizer with stop words
    vectorizer = CountVectorizer(stop_words=STOPWORDS)

    # Fit and transform the preprocessed texts to create the DTM
    dtm = vectorizer.fit_transform(preprocessed_texts)

    # Create a DataFrame from the DTM
    dtm_df = pd.DataFrame(dtm.toarray(), columns=vectorizer.get_feature_names_out())

    return dtm_df

# Example usage:
# texts = ["This is a sample document.", "Another example document is here.", "And another one."]
# dtm_df = task_func(texts)
# print(dtm_df)
import unittest
class TestCases(unittest.TestCase):
    def setUp(self):
        self.texts = [
            "Hello, world!",
            "Data science is about the extraction of knowledge from data.",
            "Machine learning is a fascinating field.",
            "Python is a versatile programming language.",
            "Stop words are filtered out in text preprocessing."
        ]
    def test_dtm_shape(self):
        """Ensure the DTM has the correct shape."""
        dtm = task_func(self.texts)
        self.assertEqual(dtm.shape[0], len(self.texts), "DTM should have one row per document.")
    def test_dtm_non_negative(self):
        """Ensure all values in the DTM are non-negative."""
        dtm = task_func(self.texts)
        self.assertTrue((dtm >= 0).all().all(), "All DTM values should be non-negative.")
    def test_stopwords_removal(self):
        """Check if common stopwords are removed."""
        dtm = task_func(["This is a test.", "Another test here."])
        self.assertNotIn("is", dtm.columns, "Stopwords should be removed from DTM columns.")
    def test_alphanumeric_filtering(self):
        """Verify that non-alphanumeric characters are filtered out."""
        dtm = task_func(["Example: test!", "#Another$% test."])
        self.assertFalse(any(char in dtm.columns for char in ":!#$%"), "Non-alphanumeric characters should be filtered out.")
    def test_lowercase_conversion(self):
        """Test if all text is converted to lowercase."""
        dtm = task_func(["LoWeR and UPPER"])
        self.assertIn("lower", dtm.columns, "All text should be converted to lowercase.")
        self.assertIn("upper", dtm.columns, "All text should be converted to lowercase.")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)