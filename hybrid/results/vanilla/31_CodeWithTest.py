import nltk
from string import punctuation
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter

# Constants
PUNCTUATION = set(punctuation)

def task_func(text):
    # Tokenize the text into words
    words = nltk.word_tokenize(text)
    
    # Filter words that start with '$' and contain more than just punctuation
    filtered_words = [word for word in words if word.startswith('$') and any(char not in PUNCTUATION for char in word[1:])]
    
    # Count the frequency of each filtered word
    word_counts = Counter(filtered_words)
    
    # If there are no valid words, return None
    if not word_counts:
        return None
    
    # Create a bar plot
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(x=list(word_counts.keys()), y=list(word_counts.values()))
    ax.set_title('Frequency of Words Starting with "$"')
    ax.set_xlabel('Words')
    ax.set_ylabel('Frequency')
    
    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)
    
    # Show the plot
    plt.tight_layout()
    plt.show()
    
    return ax

# Example usage:
# text = "The $price of $AAPL is $150. $!$ is not counted, but $USD is."
# task_func(text)
import unittest
class TestCases(unittest.TestCase):
    """Test cases for the task_func function."""
    @staticmethod
    def is_bar(ax, expected_values, expected_categories):
        extracted_values = [
            bar.get_height() for bar in ax.patches
        ]  # extract bar height
        extracted_categories = [
            tick.get_text() for tick in ax.get_xticklabels()
        ]  # extract category label
        for actual_value, expected_value in zip(extracted_values, expected_values):
            assert (
                actual_value == expected_value
            ), f"Expected value '{expected_value}', but got '{actual_value}'"
        for actual_category, expected_category in zip(
            extracted_categories, expected_categories
        ):
            assert (
                actual_category == expected_category
            ), f"Expected category '{expected_category}', but got '{actual_category}'"
    def test_case_1(self):
        # Randomly generated sentence with $ words
        text = "This is the $first $first sentence."
        plot = task_func(text)
        self.assertIsInstance(plot, plt.Axes, "Return type should be a plot (Axes).")
        self.is_bar(plot, expected_categories=["$first"], expected_values=[2.0])
    def test_case_2(self):
        # Another randomly generated sentence with $ words
        text = "This $is $is $is the $second $sentence $sentence"
        plot = task_func(text)
        self.assertIsInstance(plot, plt.Axes, "Return type should be a plot (Axes).")
        self.is_bar(
            plot,
            expected_categories=["$is", "$second", "$sentence"],
            expected_values=[3.0, 1.0, 2.0],
        )
    def test_case_3(self):
        # Sentence without any $ words
        text = "This is the third sentence."
        plot = task_func(text)
        self.assertIsNone(plot, "The plot should be None since there are no $ words.")
    def test_case_4(self):
        # Sentence with all $ words being single characters or punctuation
        text = "$ $! $@ $$"
        plot = task_func(text)
        self.assertIsNone(
            plot,
            "The plot should be None since all $ words are single characters or punctuation.",
        )
    def test_case_5(self):
        # Mix of valid $ words and punctuation-only $ words with some repeated words
        text = "$apple $apple $banana $!$ $@ fruit $cherry"
        plot = task_func(text)
        self.assertIsInstance(plot, plt.Axes, "Return type should be a plot (Axes).")
        self.is_bar(
            plot,
            expected_categories=["$apple", "$banana", "$cherry"],
            expected_values=[2.0, 1.0, 1.0],
        )


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)