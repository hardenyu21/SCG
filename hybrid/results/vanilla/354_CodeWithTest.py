import collections
import matplotlib.pyplot as plt
import pandas as pd

# Constants
WORDS = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'I']

def task_func(sentences_dict, word_keys=WORDS):
    # Initialize a counter for word occurrences
    word_counter = collections.Counter()

    # Iterate over each sentence in the dictionary
    for sentence in sentences_dict.values():
        # Split the sentence into words and update the counter
        words = sentence.lower().split()
        word_counter.update(words)

    # Filter the counter to only include the specified word keys
    filtered_counts = {word: word_counter[word] for word in word_keys}

    # Create a DataFrame for easier plotting
    df = pd.DataFrame(list(filtered_counts.items()), columns=['Word', 'Count'])

    # Plot the bar chart
    fig, ax = plt.subplots()
    ax.bar(df['Word'], df['Count'], color='skyblue')
    ax.set_xlabel('Words')
    ax.set_ylabel('Frequency')
    ax.set_title('Word Frequency in Sentences')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Return the Axes object
    return ax

# Example usage:
# sentences_dict = {
#     'sentence1': "The quick brown fox jumps over the lazy dog.",
#     'sentence2': "I have a dream that one day this nation will rise up.",
#     'sentence3': "To be or not to be, that is the question."
# }
# ax = task_func(sentences_dict)
# plt.show()
import unittest
import doctest
class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        sentences_dict = {
            'Sentence1': 'the quick brown fox',
            'Sentence2': 'jumps over the lazy dog',
            'Sentence3': 'the dog is brown'
        }
        word_keys = ['the', 'dog']
        ax = task_func(sentences_dict, word_keys)
        
        # Check the x-tick labels
        self.assertListEqual([label.get_text() for label in ax.get_xticklabels()], word_keys)
        
        # Check the bar heights
        self.assertListEqual([rect.get_height() for rect in ax.patches], [3, 2, 3, 2])
        
    def test_case_2(self):
        sentences_dict = {
            'Sentence1': 'apple orange banana',
            'Sentence2': 'apple apple',
            'Sentence3': 'banana orange orange'
        }
        word_keys = ['apple', 'orange', 'banana']
        ax = task_func(sentences_dict, word_keys)
        
        # Check the x-tick labels
        self.assertListEqual([label.get_text() for label in ax.get_xticklabels()], word_keys)
        
        # Check the bar heights
        self.assertListEqual([rect.get_height() for rect in ax.patches], [3, 3, 2, 3, 3, 2])
        
    def test_case_3(self):
        sentences_dict = {
            'Sentence1': 'cat mouse',
            'Sentence2': 'dog cat',
            'Sentence3': 'mouse mouse cat'
        }
        word_keys = ['cat', 'mouse', 'dog']
        ax = task_func(sentences_dict, word_keys)
        
        # Check the x-tick labels
        self.assertListEqual([label.get_text() for label in ax.get_xticklabels()], word_keys)
        
        # Check the bar heights
        self.assertListEqual([rect.get_height() for rect in ax.patches], [3, 3, 1, 3, 3, 1])
    def test_case_4(self):
        sentences_dict = {
            'Sentence1': 'sun moon stars',
            'Sentence2': 'sun sun',
            'Sentence3': 'moon stars stars'
        }
        word_keys = ['sun', 'stars', 'moon']
        ax = task_func(sentences_dict, word_keys)
        
        # Check the x-tick labels
        self.assertListEqual([label.get_text() for label in ax.get_xticklabels()], word_keys)
        
        # Check the bar heights
        self.assertListEqual([rect.get_height() for rect in ax.patches], [3, 3, 2, 3, 3, 2])
    def test_case_5(self):
        sentences_dict = {
            'Sentence1': 'car bus bike',
            'Sentence2': 'bus bus bike',
            'Sentence3': 'car car bus'
        }
        word_keys = ['car', 'bus', 'bike']
        ax = task_func(sentences_dict, word_keys)
        
        # Check the x-tick labels
        self.assertListEqual([label.get_text() for label in ax.get_xticklabels()], word_keys)
        
        # Check the bar heights
        self.assertListEqual([rect.get_height() for rect in ax.patches], [3, 4, 2, 3, 4, 2])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)