import re
import matplotlib.pyplot as plt
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk

# Ensure you have the necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

def task_func(example_str, top_n=30):
    # Remove text enclosed in square brackets
    cleaned_str = re.sub(r'\[.*?\]', '', example_str)
    
    # Tokenize the text into words
    words = word_tokenize(cleaned_str)
    
    # Convert to lowercase and filter out stopwords and non-alphabetic tokens
    stop_words = set(stopwords.words('english'))
    filtered_words = [word.lower() for word in words if word.isalpha() and word.lower() not in stop_words]
    
    # Create a frequency distribution
    freq_dist = FreqDist(filtered_words)
    
    # Plot the frequency distribution
    fig, ax = plt.subplots(figsize=(10, 6))
    freq_dist.plot(top_n, cumulative=False, ax=ax)
    plt.title('Word Frequency Distribution')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.show()
    
    # Get the top_n most common words
    top_words = freq_dist.most_common(top_n)
    top_words_dict = {word: freq for word, freq in top_words}
    
    return ax, top_words_dict

# Example usage:
# ax, top_words = task_func("This is a sample text [with some text in brackets] and some more text.")
# print(top_words)
import unittest
import doctest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        example_str = "Josie Smith [3996 COLLEGE AVENUE, SOMETOWN, MD 21003] Mugsy Dog Smith [2560 OAK ST, GLENMEADE, WI 14098]"
        ax, top_n_words = task_func(example_str)
        self.assertIsInstance(ax, plt.Axes, "The returned object is not of type plt.Axes.")
        # Test the number of words in the plot
        self.assertEqual(len(ax.get_xticklabels()), 4, "The number of words in the plot is not 30.")
        # Test the top_n_words dictionary
        self.assertEqual(top_n_words, {'Smith': 2, 'Josie': 1, 'Mugsy': 1, 'Dog': 1}, "The top_n_words dictionary is incorrect.")
    def test_case_2(self):
        example_str = "Hello [1234 STREET, CITY, STATE 12345] World [5678 LANE, TOWN, PROVINCE 67890]"
        ax, _ = task_func(example_str)
        self.assertIsInstance(ax, plt.Axes, "The returned object is not of type plt.Axes.")
    def test_case_3(self):
        example_str = "[IGNORE THIS] This is a simple test string [ANOTHER IGNORE]"
        ax, top_n_words = task_func(example_str, top_n=5)
        self.assertIsInstance(ax, plt.Axes, "The returned object is not of type plt.Axes.")
        # Test the histogram data
        #self.assertEqual(len(ax.patches), 5, "The number of words in the plot is not 5.")
        # Test the top_n_words dictionary
        self.assertEqual(top_n_words, {'This': 1, 'is': 1, 'a': 1, 'simple': 1, 'test': 1}, "The top_n_words dictionary is incorrect.")
    
    def test_case_4(self):
        example_str = "[BEGIN] Testing the function with different [MIDDLE] types of input strings [END]"
        ax, _ = task_func(example_str)
        self.assertIsInstance(ax, plt.Axes, "The returned object is not of type plt.Axes.")
    
    def test_case_5(self):
        example_str = "Example without any brackets so all words should be considered."
        ax, _ = task_func(example_str)
        self.assertIsInstance(ax, plt.Axes, "The returned object is not of type plt.Axes.")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)