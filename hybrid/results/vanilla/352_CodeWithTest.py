import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

def task_func(text_dict, word_keys, top_k=2):
    # Validate top_k
    if top_k < 0:
        raise ValueError("top_k must be a non-negative integer.")
    
    # Calculate frequencies for the provided word_keys
    word_frequencies = {word: text_dict.get(word, 0) for word in word_keys}
    
    # Get the top_k most common words and their frequencies
    counter = Counter(text_dict)
    top_k_common_words = counter.most_common(top_k)
    top_k_frequencies = {word: freq for word, freq in top_k_common_words}
    
    # Create a bar chart
    fig, ax = plt.subplots()
    ax.bar(word_frequencies.keys(), word_frequencies.values(), color='skyblue')
    ax.set_xlabel('Words')
    ax.set_ylabel('Frequencies')
    ax.set_title('Word Frequencies')
    plt.xticks(rotation=45)
    
    # Return the Axes object and the dictionary of top_k frequencies
    return ax, top_k_frequencies

# Example usage:
# text_dict = {'apple': 4, 'banana': 2, 'orange': 5, 'grape': 3}
# word_keys = ['apple', 'banana', 'kiwi']
# ax, top_k_frequencies = task_func(text_dict, word_keys, top_k=3)
# plt.show()
# print(top_k_frequencies)
import unittest
import doctest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        text_dict = Counter(['the', 'be', 'to', 'the', 'and', 'that', 'a', 'in', 'the', 'that', 'have', 'I'])
        word_keys = ['the', 'and', 'I']
        ax, top_k_dict = task_func(text_dict, word_keys, 3)
        self.assertDictContainsSubset(top_k_dict, {'the': 3, 'that': 2, 'be': 1})
        self.assertEqual(ax.get_xticks().tolist(), list(range(len(word_keys))))
        self.assertEqual([label.get_text() for label in ax.get_xticklabels()], word_keys)
    def test_case_2(self):
        text_dict = Counter(['apple', 'banana', 'apple', 'orange', 'grape', 'apple', 'banana'])
        word_keys = ['apple', 'banana', 'cherry']
        ax, top_k_dict = task_func(text_dict, word_keys)
        self.assertDictContainsSubset(top_k_dict, {'apple': 3, 'banana': 2})
        self.assertEqual(ax.get_xticks().tolist(), list(range(len(word_keys))))
        self.assertEqual([label.get_text() for label in ax.get_xticklabels()], word_keys)
    def test_case_3(self):
        text_dict = Counter([])
        word_keys = ['apple', 'banana', 'cherry']
        ax, top_k_dict = task_func(text_dict, word_keys)
        self.assertEqual(ax.get_xticks().tolist(), list(range(len(word_keys))))
        self.assertEqual([label.get_text() for label in ax.get_xticklabels()], word_keys)
    def test_case_4(self):
        text_dict = Counter(['a', 'a', 'b', 'b', 'b', 'c', 'c'])
        word_keys = ['a', 'b', 'c', 'd']
        ax, top_k_dict = task_func(text_dict, word_keys)
        self.assertEqual(ax.get_xticks().tolist(), list(range(len(word_keys))))
        self.assertEqual([label.get_text() for label in ax.get_xticklabels()], word_keys)
    def test_case_5(self):
        text_dict = Counter(['cat', 'dog', 'cat', 'fish', 'fish', 'fish', 'bird'])
        word_keys = ['cat', 'dog', 'bird', 'elephant']
        ax, top_k_dict = task_func(text_dict, word_keys,9)
        self.assertDictContainsSubset(top_k_dict, {'fish': 3, 'cat': 2, 'dog': 1, 'bird': 1})
        self.assertEqual(ax.get_xticks().tolist(), list(range(len(word_keys))))
        self.assertEqual([label.get_text() for label in ax.get_xticklabels()], word_keys)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)