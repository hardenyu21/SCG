import numpy as np
import matplotlib.pyplot as plt
import string

# Constants
ALPHABET = list(string.ascii_lowercase)

def task_func(word):
    # Convert the word to lowercase to ensure case insensitivity
    word = word.lower()
    
    # Get the positions of each letter in the word
    positions = [ALPHABET.index(letter) + 1 for letter in word if letter in ALPHABET]
    
    # Create a bar chart
    fig, ax = plt.subplots()
    ax.bar(range(len(word)), positions, tick_label=list(word))
    
    # Set labels and title
    ax.set_xlabel('Letters in the word')
    ax.set_ylabel('Position in the alphabet')
    ax.set_title('Alphabet Positions of Letters in the Word')
    
    # Show the plot
    plt.show()
    
    return ax

# Example usage:
# ax = task_func("example")
import unittest
from matplotlib.axes import Axes
class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        ax = task_func('abc')
        self.assertIsInstance(ax, Axes, "The returned object is not an instance of Axes.")
        self.assertEqual(ax.patches[0].get_height(), 1, "The height of the first bar should be 1.")
        self.assertEqual(ax.patches[1].get_height(), 2, "The height of the second bar should be 2.")
        self.assertEqual(ax.patches[2].get_height(), 3, "The height of the third bar should be 3.")
    
    def test_case_2(self):
        ax = task_func('xyz')
        self.assertIsInstance(ax, Axes, "The returned object is not an instance of Axes.")
        self.assertEqual(ax.patches[0].get_height(), 24, "The height of the first bar should be 24.")
        self.assertEqual(ax.patches[1].get_height(), 25, "The height of the second bar should be 25.")
        self.assertEqual(ax.patches[2].get_height(), 26, "The height of the third bar should be 26.")
        
    def test_case_3(self):
        ax = task_func('ace')
        self.assertIsInstance(ax, Axes, "The returned object is not an instance of Axes.")
        self.assertEqual(ax.patches[0].get_height(), 1, "The height of the first bar should be 1.")
        self.assertEqual(ax.patches[1].get_height(), 3, "The height of the second bar should be 3.")
        self.assertEqual(ax.patches[2].get_height(), 5, "The height of the third bar should be 5.")
        
    def test_case_4(self):
        ax = task_func('bd')
        self.assertIsInstance(ax, Axes, "The returned object is not an instance of Axes.")
        self.assertEqual(ax.patches[0].get_height(), 2, "The height of the first bar should be 2.")
        self.assertEqual(ax.patches[1].get_height(), 4, "The height of the second bar should be 4.")
        
    def test_case_5(self):
        with self.assertRaises(ValueError):
            task_func('a1b')


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)