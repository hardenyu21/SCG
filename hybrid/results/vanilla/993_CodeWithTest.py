import re
from scipy.stats import gaussian_kde
import matplotlib.pyplot as plt

def task_func(text):
    # Extract words from the text
    words = re.findall(r'\b\w+\b', text)
    
    # Calculate the lengths of the words
    word_lengths = [len(word) for word in words]
    
    # Create a subplot
    fig, ax = plt.subplots()
    
    # Plot the histogram of word lengths
    ax.hist(word_lengths, bins=range(1, max(word_lengths) + 2), alpha=0.6, color='g', edgecolor='black', density=True)
    
    # If there are more than one unique word lengths, plot the KDE
    if len(set(word_lengths)) > 1:
        kde = gaussian_kde(word_lengths)
        x = range(1, max(word_lengths) + 1)
        ax.plot(x, kde(x), color='r', label='KDE')
        ax.legend()
    
    # Set labels and title
    ax.set_xlabel('Word Length')
    ax.set_ylabel('Density')
    ax.set_title('Distribution of Word Lengths')
    
    # Show the plot
    plt.show()
    
    return ax
import unittest
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
class TestCases(unittest.TestCase):
    """Tests for the task_func function"""
    def test_simple_sentence(self):
        """Test a simple sentence"""
        ax1 = task_func("This is a test")
        self.assertIsInstance(ax1, plt.Axes)
        # The number of bars might differ due to matplotlib's binning strategy
        unique_word_lengths = {len(word) for word in "This is a test".split() if word}
        self.assertTrue(
            len(ax1.patches) >= len(unique_word_lengths),
            "Incorrect number of bars for a simple sentence",
        )
    def test_empty_string(self):
        """Test an empty string"""
        ax2 = task_func("")
        self.assertIsInstance(ax2, plt.Axes)
        self.assertEqual(
            len(ax2.patches), 0, "There should be no bars for an empty string"
        )
    def test_special_characters(self):
        """Test special characters and numbers"""
        ax3 = task_func("Hello, world! 1234")
        self.assertIsInstance(ax3, plt.Axes)
        # The number of bars might differ due to matplotlib's binning strategy
        unique_word_lengths = {
            len(word) for word in "Hello, world! 1234".split() if word
        }
        self.assertTrue(
            len(ax3.patches) >= len(unique_word_lengths),
            "Incorrect handling of special characters and numbers",
        )
    def test_repeated_words(self):
        """Test repeated words"""
        ax4 = task_func("repeat repeat repeat")
        self.assertIsInstance(ax4, plt.Axes)
        # Only one unique word length: 6
        self.assertTrue(len(ax4.patches) >= 1, "Incorrect handling of repeated words")
    def test_long_text(self):
        """Test a long text"""
        text = "A long text with multiple words of different lengths"
        ax5 = task_func(text)
        self.assertIsInstance(ax5, plt.Axes)
        # Adjust expectation for number of bars due to matplotlib's binning
        words = re.split(r"\W+", text)
        word_counts = pd.Series([len(word) for word in words if word])
        expected_unique_lengths = len(set(word_counts))
        self.assertTrue(
            len(ax5.patches) >= expected_unique_lengths,
            "Incorrect plot for a long text",
        )
    def tearDown(self):
        plt.clf()


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)