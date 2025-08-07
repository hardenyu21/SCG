import seaborn as sns
import matplotlib.pyplot as plt
import random

def task_func(list_of_lists, seed=0):
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # Fill empty sublists with 5 random integers ranging from 0 to 100
    for sublist in list_of_lists:
        if not sublist:
            sublist.extend(random.randint(0, 100) for _ in range(5))
    
    # Combine all sublists into a single list
    combined_data = [item for sublist in list_of_lists for item in sublist]
    
    # Create a histogram using seaborn
    plt.figure(figsize=(10, 6))
    ax = sns.histplot(combined_data, bins=20, kde=True)
    
    # Set plot title and labels
    ax.set_title('Histogram of Combined Data')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    
    # Show the plot
    plt.show()
    
    # Return the Axes object
    return ax
import unittest
import doctest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Input: Two non-empty sublists and one empty sublist
        plot = task_func([[1, 2, 3], [], [4, 5, 6]])
        self.assertEqual(str(type(plot)), "<class 'matplotlib.axes._axes.Axes'>")
        # Test the number of bars in the histogram
        self.assertEqual(len(plot.patches), 5)
    def test_case_2(self):
        # Input: All empty sublists
        plot = task_func([[], [], []])
        self.assertEqual(str(type(plot)), "<class 'matplotlib.axes._axes.Axes'>")
    def test_case_3(self):
        # Input: Single non-empty sublist
        plot = task_func([[1, 2, 3, 4, 5]], 77)
        self.assertEqual(str(type(plot)), "<class 'matplotlib.axes._axes.Axes'>")
        # Test the number of bars in the histogram
        self.assertEqual(len(plot.patches), 4)
    def test_case_4(self):
        # Input: Single empty sublist
        plot = task_func([[]])
        self.assertEqual(str(type(plot)), "<class 'matplotlib.axes._axes.Axes'>")
    def test_case_5(self):
        # Input: Mixed empty and non-empty sublists
        plot = task_func([[10, 20], [], [30, 40, 50], []])
        self.assertEqual(str(type(plot)), "<class 'matplotlib.axes._axes.Axes'>")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)