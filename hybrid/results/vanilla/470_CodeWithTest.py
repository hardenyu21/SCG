import matplotlib.pyplot as plt
import numpy as np

def task_func(myList):
    # Determine the range of the data
    min_val = np.floor(min(myList))
    max_val = np.ceil(max(myList))
    
    # Create bin edges that align with integer values
    bins = np.arange(min_val, max_val + 1) - 0.5
    
    # Create the histogram
    fig, ax = plt.subplots()
    ax.hist(myList, bins=bins, edgecolor='black')
    
    # Set labels and title
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram of Values')
    
    # Return the Axes object
    return ax
import unittest
import numpy as np
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test basic case
        myList = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
        ax = task_func(myList)
        heights, _, _ = ax.hist(
            myList,
            bins=np.arange(min(myList), max(myList) + 2) - 0.5,
            edgecolor="black",
        )
        self.assertIsInstance(ax, plt.Axes)
        self.assertListEqual(list(heights), [1, 2, 3, 4])
        self.assertEqual(ax.get_title(), "Histogram of Values")
        self.assertEqual(ax.get_xlabel(), "Value")
        self.assertEqual(ax.get_ylabel(), "Frequency")
    def test_case_2(self):
        # Test with empty list
        with self.assertRaises(ValueError):
            task_func([])
    def test_case_3(self):
        # Test with single element
        myList = [100]
        ax = task_func(myList)
        heights, _, _ = ax.hist(myList)
        self.assertEqual(heights.max(), 1)
    def test_case_4(self):
        # Test with negative values
        myList = [-5, -4, -3, -3, -2, -2, -2, -1]
        ax = task_func(myList)
        heights, _, _ = ax.hist(myList)
        self.assertGreaterEqual(len(heights), 1)
    def test_case_5(self):
        # Test with floats
        myList = [1.1, 1.2, 2.5, 2.5, 3.75, 4.25]
        ax = task_func(myList)
        heights, _, _ = ax.hist(myList)
        self.assertGreaterEqual(len(heights), 1)
    def test_case_6(self):
        # Test handling non-numeric values
        myList = ["a", "b", "c"]
        with self.assertRaises(TypeError):
            task_func(myList)
    def tearDown(self):
        plt.close("all")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)