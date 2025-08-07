import numpy as np
import matplotlib.pyplot as plt
import itertools

def task_func(data_list):
    # Check if the data_list is empty
    if not data_list:
        raise ValueError("The data_list is empty.")
    
    # Unzip the list of tuples
    unzipped_data = list(itertools.zip_longest(*data_list))
    
    # Plot the numerical values for each position
    fig, ax = plt.subplots()
    for i, data in enumerate(unzipped_data):
        ax.plot(data, label=f'Position {i}')
    
    # Add labels and legend
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    ax.legend()
    
    # Show the plot
    plt.show()
    
    return ax
import unittest
import doctest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        data_list = [('a', 1, 2), ('b', 2, 3), ('c', 3, 4), ('d', 4, 5), ('e', 5, 6)]
        plot = task_func(data_list)
        self.assertIsInstance(plot, type(plt.gca()))
    def test_case_2(self):
        data_list = [('a', 6, 7), ('b', 7, 8), ('c', 8, 9)]
        plot = task_func(data_list)
        self.assertIsInstance(plot, type(plt.gca()))
        # Test the plot data
        self.assertEqual(len(plot.lines), 2)
    def test_case_3(self):
        data_list = []
        with self.assertRaises(ValueError):  # Expecting a ValueError due to empty data_list
            task_func(data_list)
    def test_case_4(self):
        data_list = [('a', 10, 11), ('b', 11, 12), ('c', 12, 13), ('d', 13, 14)]
        plot = task_func(data_list)
        self.assertIsInstance(plot, type(plt.gca()))
        # Test the plot data array
        self.assertEqual(len(plot.lines), 2)
        # Test the plot limits
        self.assertAlmostEqual(plot.get_xlim()[0], -0.15, places=1)
        self.assertAlmostEqual(plot.get_xlim()[1], 3.15, places=1)
    def test_case_5(self):
        data_list = [('a', np.nan, np.nan), ('b', np.nan, np.nan)]
        plot = task_func(data_list)
        self.assertIsInstance(plot, type(plt.gca()))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)