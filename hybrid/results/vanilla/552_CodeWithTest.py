import collections
import itertools
import matplotlib.pyplot as plt

# Constants
ITEMS = ['apple', 'banana']

def task_func(a, b, items=ITEMS):
    # Combine the two lists
    combined_list = list(itertools.chain(a, b))
    
    # Count the frequency of each item in the combined list
    frequency_counter = collections.Counter(combined_list)
    
    # Extract the frequencies of the predefined items
    item_frequencies = [frequency_counter[item] for item in items]
    
    # Create a bar chart
    fig, ax = plt.subplots()
    ax.bar(items, item_frequencies)
    
    # Set labels and title
    ax.set_xlabel('Items')
    ax.set_ylabel('Frequency')
    ax.set_title('Frequency of Predefined Items in Combined List')
    
    # Show the plot
    plt.show()
    
    return ax

# Example usage:
# list1 = ['apple', 'banana', 'apple', 'orange']
# list2 = ['banana', 'apple', 'grape', 'banana']
# task_func(list1, list2)
import unittest
import matplotlib
class TestCases(unittest.TestCase):
    def test_standard_functionality(self):
        """Test with typical list inputs."""
        a = ['apple', 'banana', 'cherry']
        b = ['banana', 'apple', 'apple', 'dragonfruit']
        ax = task_func(a, b)
        self.assertIsInstance(ax, plt.Axes)
    def test_empty_lists(self):
        """Test with both lists empty."""
        a = []
        b = []
        ax = task_func(a, b)
        self.assertIsInstance(ax, plt.Axes)
    def test_one_empty_list(self):
        """Test with one list empty."""
        a = ['apple', 'apple']
        b = []
        ax = task_func(a, b)
        self.assertIsInstance(ax, plt.Axes)
    def test_non_predefined_items_only(self):
        """Test with lists containing non-predefined items."""
        a = ['cherry', 'dragonfruit']
        b = ['cherry', 'mango']
        ax = task_func(a, b)
        self.assertIsInstance(ax, plt.Axes)
    def test_all_predefined_items(self):
        """Test with lists containing only predefined items."""
        a = ['apple', 'apple']
        b = ['banana']
        ax = task_func(a, b)
        self.assertIsInstance(ax, plt.Axes)
    def test_duplicate_items(self):
        """Test with lists containing duplicate items."""
        a = ['apple', 'apple']
        b = ['apple', 'banana', 'banana']
        ax = task_func(a, b)
        self.assertIsInstance(ax, plt.Axes)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)