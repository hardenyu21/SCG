import itertools
import numpy as np
import matplotlib.pyplot as plt

def task_func(elements, subset_size):
    # Generate all subsets of the given size
    subsets = list(itertools.combinations(elements, subset_size))
    
    # Calculate the sum of each subset
    subset_sums = [sum(subset) for subset in subsets]
    
    # Plot a histogram of the sums
    fig, ax = plt.subplots()
    ax.hist(subset_sums, bins='auto', alpha=0.7, color='blue', edgecolor='black')
    ax.set_title('Histogram of Subset Sums')
    ax.set_xlabel('Sum of Subset')
    ax.set_ylabel('Frequency')
    
    # Return the Axes object, list of subsets, and list of subset sums
    return ax, subsets, subset_sums

# Example usage:
# elements = (1, 2, 3, 4)
# subset_size = 2
# ax, subsets, subset_sums = task_func(elements, subset_size)
# plt.show()
import unittest
import doctest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Testing with a tuple of size 10 and subset size 2
        ax, combs, sums = task_func((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 2)
        self.assertIsInstance(ax, plt.Axes)  # Check if the return type is correct
        # Test the combinations and sums
        self.assertEqual(len(combs), 45)
        self.assertEqual(len(sums), 45)
    def test_case_2(self):
        # Testing with a tuple of size 5 and subset size 3
        ax, combs, sums = task_func((2, 4, 6, 8, 10), 3)
        self.assertIsInstance(ax, plt.Axes)
        # Test the combinations and sums
        self.assertEqual(len(combs), 10)
        self.assertEqual(len(sums), 10)
    def test_case_3(self):
        # Testing with an empty tuple
        ax, combs, sums = task_func((), 0)
        self.assertIsInstance(ax, plt.Axes)
    def test_case_4(self):
        # Testing with negative numbers in the tuple
        ax, combs, sums = task_func((-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5), 2)
        self.assertIsInstance(ax, plt.Axes)
    def test_case_5(self):
        # Testing with a subset size of 0
        ax, combs, sums = task_func((1, 2, 3, 4, 5), 2)
        self.assertIsInstance(ax, plt.Axes)
        # Test the combinations and sums
        self.assertEqual(combs, [(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)])
        self.assertEqual(sums, [3, 4, 5, 6, 5, 6, 7, 7, 8, 9])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)