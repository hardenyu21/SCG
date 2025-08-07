# Importing the required libraries
import re
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
import nltk

# Ensure the stopwords are downloaded
nltk.download('stopwords')

def task_func(text, n=2):
    # Remove duplicate consecutive words
    text = re.sub(r'\b(\w+)( \1\b)+', r'\1', text)
    
    # Tokenize the text
    words = text.split()
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.lower() not in stop_words]
    
    # Create a co-occurrence matrix
    vectorizer = CountVectorizer(ngram_range=(1, n), binary=True)
    X = vectorizer.fit_transform([' '.join(filtered_words)])
    feature_names = vectorizer.get_feature_names_out()
    
    # Create a square co-occurrence matrix
    co_occurrence_matrix = (X.T * X)
    co_occurrence_matrix.setdiag(0)  # Set diagonal to zero to ignore self-co-occurrence
    
    # Convert to DataFrame
    df_co_occurrence = pd.DataFrame(co_occurrence_matrix.toarray(), index=feature_names, columns=feature_names)
    
    # Plot the co-occurrence matrix
    plt.figure(figsize=(10, 8))
    ax = plt.matshow(df_co_occurrence, fignum=1, cmap='Blues')
    plt.xticks(range(len(feature_names)), feature_names, rotation=90)
    plt.yticks(range(len(feature_names)), feature_names)
    plt.colorbar(ax)
    plt.title('Co-occurrence Matrix')
    
    # Return the DataFrame and the Axes object
    return df_co_occurrence, ax

# Example usage
text = "This is a test text with some duplicate words and some stopwords. This text is for testing."
df, ax = task_func(text)
plt.show()
import unittest
class TestCases(unittest.TestCase):
    def test_simple_text(self):
        """Test with a simple text."""
        text = "hello world"
        matrix, _ = task_func(text)
        self.assertEqual(matrix.shape, (1, 1), "Matrix shape should be (1, 1) for unique words 'hello' and 'world'.")
    def test_text_with_stopwords(self):
        """Test text with stopwords removed."""
        text = "this is a"
        matrix, _ = task_func(text)
        self.assertTrue(matrix.empty, "Matrix should be empty after removing stopwords.")
    def test_duplicate_words(self):
        """Test text with duplicate consecutive words."""
        text = "happy happy joy joy"
        matrix, _ = task_func(text)
        self.assertIn('happy joy', matrix.columns, "Matrix should contain 'happy joy' after duplicates are removed.")
    def test_ngram_range(self):
        """Test with a specific n-gram range."""
        text = "jump high and run fast"
        # Assuming no preprocessing that removes words, we expect 3 unique tri-grams.
        matrix, _ = task_func(text, n=3)
        # Expecting a 3x3 matrix since there are 3 unique tri-grams with no overlap in this simple case.
        self.assertEqual(matrix.shape, (2, 2),
                         "Matrix shape should be (3, 3) for a tri-gram analysis without word removal.")
    def test_empty_text(self):
        """Test with an empty string."""
        text = ""
        matrix, _ = task_func(text)
        self.assertTrue(matrix.empty, "Matrix should be empty for an empty string.")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)