import math
import numpy as np
import matplotlib.pyplot as plt

def task_func(list_input):
    # Sort the list based on the degree value of its elements
    sorted_list = sorted(list_input, key=lambda x: math.degrees(x))
    
    # Calculate the cumulative sum of the sorted list
    cumulative_sum = np.cumsum(sorted_list)
    
    # Plot the cumulative sum
    fig, ax = plt.subplots()
    ax.plot(cumulative_sum, marker='o')
    ax.set_title('Cumulative Sum of Sorted List')
    ax.set_xlabel('Index')
    ax.set_ylabel('Cumulative Sum')
    
    # Return the cumulative sum and the Axes object
    return cumulative_sum, ax

# Example usage:
# list_input = [math.radians(30), math.radians(60), math.radians(45)]
# cumulative_sum, ax = task_func(list_input)
# plt.show()
import unittest
import doctest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        cumsum, ax = task_func([10, 20, 30])
        self.assertListEqual(list(cumsum), [10, 30, 60])
        self.assertEqual(ax.get_title(), 'Cumulative Sum Plot')
        self.assertEqual(ax.get_xlabel(), 'Index')
        self.assertEqual(ax.get_ylabel(), 'Cumulative Sum')
    def test_case_2(self):
        cumsum, ax = task_func([5, 15, 25])
        self.assertListEqual(list(cumsum), [5, 20, 45])
        self.assertEqual(ax.get_title(), 'Cumulative Sum Plot')
        self.assertEqual(ax.get_xlabel(), 'Index')
        self.assertEqual(ax.get_ylabel(), 'Cumulative Sum')
    def test_case_3(self):
        cumsum, ax = task_func([])
        self.assertListEqual(list(cumsum), [])
        self.assertEqual(ax.get_title(), 'Cumulative Sum Plot')
        self.assertEqual(ax.get_xlabel(), 'Index')
        self.assertEqual(ax.get_ylabel(), 'Cumulative Sum')
    def test_case_4(self):
        cumsum, ax = task_func([1, 2, 3, 4, 5])
        self.assertListEqual(list(cumsum), [1, 3, 6, 10, 15])
        self.assertEqual(ax.get_title(), 'Cumulative Sum Plot')
        self.assertEqual(ax.get_xlabel(), 'Index')
        self.assertEqual(ax.get_ylabel(), 'Cumulative Sum')
    def test_case_5(self):
        cumsum, ax = task_func([5])
        self.assertListEqual(list(cumsum), [5])
        self.assertEqual(ax.get_title(), 'Cumulative Sum Plot')
        self.assertEqual(ax.get_xlabel(), 'Index')
        self.assertEqual(ax.get_ylabel(), 'Cumulative Sum')


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)