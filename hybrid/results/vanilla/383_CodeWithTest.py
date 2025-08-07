import pandas as pd
import seaborn as sns
from collections import Counter
from textblob import TextBlob
from matplotlib import pyplot as plt

def task_func(text, n, top_k):
    # Tokenize the text into n-grams
    blob = TextBlob(text)
    ngrams = blob.ngrams(n=n)
    
    # Count the frequency of each n-gram
    ngram_counts = Counter(ngrams)
    
    # Get the top K n-grams
    top_ngrams = ngram_counts.most_common(top_k)
    
    # Convert the top n-grams to a DataFrame for visualization
    df = pd.DataFrame(top_ngrams, columns=['N-gram', 'Frequency'])
    
    # Plot the top K n-grams
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Frequency', y='N-gram', data=df, palette='viridis')
    plt.title(f'Top {top_k} {n}-grams')
    plt.xlabel('Frequency')
    plt.ylabel('N-gram')
    plt.show()

# Example usage:
# task_func("This is a test. This test is only a test.", 2, 3)
import unittest
import matplotlib.pyplot as plt
import doctest
class TestCases(unittest.TestCase):
    def tearDown(self) -> None:
        plt.close('all')
    def test_case_1(self):
        # Test with a simple text, bigram (n=2) and top 2 n-grams
        ax = task_func('This is a sample text for testing.', 2, 2)
        ngrams = [label.get_text() for label in ax.get_xticklabels()]
        self.assertNotIn('sample text', ngrams)
        self.assertIn('is a', ngrams)
    def test_case_2(self):
        # Test with a longer text, trigram (n=3) and top 3 n-grams
        text = 'The sun shines bright in the clear blue sky. The sky is blue and beautiful.'
        ax = task_func(text, 3, 3)
        ngrams = [label.get_text() for label in ax.get_xticklabels()]
        self.assertNotIn('the clear blue', ngrams)
        self.assertNotIn('sky the sky', ngrams)
        self.assertIn('the sun shines', ngrams)
    def test_case_3(self):
        # Test with no repeating n-grams, unigram (n=1) and top 3 n-grams
        text = 'Each word is unique.'
        ax = task_func(text, 1, 3)
        ngrams = [label.get_text() for label in ax.get_xticklabels()]
        self.assertEqual(len(ngrams), 3)  # Only 4 unique words bu top 3 n-grams
    def test_case_4(self):
        # Test with a repeated word, bigram (n=2) and top 1 n-grams
        text = 'Repeat repeat repeat again.'
        ax = task_func(text, 2, 1)
        ngrams = [label.get_text() for label in ax.get_xticklabels()]
        self.assertIn('repeat repeat', ngrams)
    def test_case_5(self):
        # Test with punctuation in text, bigram (n=2) and top 3 n-grams
        text = 'Hello, world! How are you, world?'
        ax = task_func(text, 2, 3)
        ngrams = [label.get_text() for label in ax.get_xticklabels()]
        self.assertIn('hello world', ngrams)
        self.assertNotIn('you world', ngrams)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)