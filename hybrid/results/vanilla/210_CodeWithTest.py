import collections
from operator import itemgetter
import matplotlib.pyplot as plt

def task_func(data):
    # Count the frequency of each letter in the dataset
    letter_counts = collections.Counter(data)
    
    # Find the letter with the maximum integer value
    max_value_letter = max(letter_counts.items(), key=itemgetter(1))[0]
    
    # Prepare data for plotting
    letters = list(letter_counts.keys())
    counts = list(letter_counts.values())
    
    # Create the bar plot
    fig, ax = plt.subplots()
    bars = ax.bar(letters, counts, label='Letter Counts')
    
    # Highlight the letter with the maximum value
    for bar, letter in zip(bars, letters):
        if letter == max_value_letter:
            bar.set_color('red')
    
    # Set labels and title
    ax.set_xlabel('Letter')
    ax.set_ylabel('Count')
    ax.set_title('Letter Counts with Max Value Letter Highlighted')
    
    # Add legend
    ax.legend()
    
    # Show the plot
    plt.show()
    
    return ax
import unittest
import doctest
class TestCases(unittest.TestCase):
    def setUp(self):
        self.data = [('a', 10), ('b', 15), ('a', 5), ('c', 20), ('b', 10)]
        self.ax = task_func(self.data)
    def test_case_1(self):
        """Test if the number of bars in the plot matches the number of unique letters in the dataset."""
        self.assertEqual(len([rect for rect in self.ax.patches]), len(set([item[0] for item in self.data]))+1)
    def test_case_2(self):
        """Test if the letter with the maximum value is correctly highlighted."""
        max_value_letter = max(self.data, key=lambda item: item[1])[0]
        for rect in self.ax.patches:
            if rect.get_label() == 'Max Value Letter':
                self.assertEqual(rect.get_x(), ord(max_value_letter) - ord('a'))
    def test_case_3(self):
        """Test if the plot has correct labels, title, and legend."""
        self.assertEqual(self.ax.get_xlabel(), 'Letter')
        self.assertEqual(self.ax.get_ylabel(), 'Count')
        self.assertEqual(self.ax.get_title(), 'Letter Counts with Max Value Letter Highlighted')
        self.assertTrue(self.ax.get_legend() is not None)
    def test_case_4(self):
        """Test if the frequency counts for each letter are correct."""
        from collections import Counter
        letter_freq = Counter([item[0] for item in self.data])
        for rect in self.ax.patches:
            if rect.get_label() == 'Letter Counts':
                self.assertEqual(rect.get_height(), letter_freq[chr(int(rect.get_x()) + ord('a'))])
    def test_case_5(self):
        """Test if non-maximum value letters are not highlighted."""
        max_value_letter = max(self.data, key=lambda item: item[1])[0]
        non_max_letters = set([item[0] for item in self.data if item[0] != max_value_letter])
        for rect in self.ax.patches:
            if rect.get_label() == 'Letter Counts' and chr(int(rect.get_x()) + ord('a')) in non_max_letters:
                self.assertNotEqual(rect.get_facecolor(), 'red')


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)