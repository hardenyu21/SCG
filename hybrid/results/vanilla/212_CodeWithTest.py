import numpy as np
from operator import itemgetter
import matplotlib.pyplot as plt

def task_func(data):
    # Extract x and y values from the data
    x_values, y_values = zip(*data)
    
    # Find the point with the maximum y-value
    max_y_point = max(data, key=itemgetter(1))
    
    # Create a scatter plot
    fig, ax = plt.subplots()
    ax.scatter(x_values, y_values, label='Data Points')
    
    # Highlight the point with the maximum y-value
    ax.scatter(max_y_point[0], max_y_point[1], color='red', zorder=5, label='Max Y Point')
    
    # Set labels and title
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Points with Max Y Point Highlighted')
    ax.legend()
    
    # Return the axes object and the maximum y-value point
    return ax, max_y_point

# Example usage:
# data = [(1, 2), (2, 3), (3, 5), (4, 1)]
# ax, max_y_point = task_func(data)
# plt.show()
# print("Max Y Point:", max_y_point)
import unittest
import doctest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Testing with three points where the third point has the highest y-value
        ax, _ = task_func([(0.1, 0.2), (0.5, 0.6), (0.3, 0.9)])
        self.assertEqual(ax.get_title(), 'Points with Max Y Point Highlighted')
        self.assertEqual(ax.get_xlabel(), 'x')
        self.assertEqual(ax.get_ylabel(), 'y')
        
    def test_case_2(self):
        # Testing with another set of points
        ax, _ = task_func([(0.2, 0.3), (0.6, 0.7), (0.4, 0.8)])
        self.assertEqual(ax.get_title(), 'Points with Max Y Point Highlighted')
        self.assertEqual(ax.get_xlabel(), 'x')
        self.assertEqual(ax.get_ylabel(), 'y')
        
    def test_case_3(self):
        # Testing with another set of points
        ax, max_y_point = task_func([(0.3, 0.4), (0.7, 0.8), (0.5, 0.7)])
        self.assertEqual(ax.get_title(), 'Points with Max Y Point Highlighted')
        self.assertEqual(ax.get_xlabel(), 'x')
        self.assertEqual(ax.get_ylabel(), 'y')
        self.assertEqual(max_y_point, (0.7, 0.8))
        
    def test_case_4(self):
        # Testing with another set of points
        ax, max_y_point = task_func([(0.4, 0.5), (0.8, 0.9), (0.6, 0.6)])
        self.assertEqual(ax.get_title(), 'Points with Max Y Point Highlighted')
        self.assertEqual(ax.get_xlabel(), 'x')
        self.assertEqual(ax.get_ylabel(), 'y')
        self.assertEqual(max_y_point, (0.8, 0.9))
    def test_case_5(self):
        # Testing with another set of points
        ax, max_y_point = task_func([(0.5, 0.6), (0.9, 0.1), (0.7, 0.5)])
        self.assertEqual(ax.get_title(), 'Points with Max Y Point Highlighted')
        self.assertEqual(ax.get_xlabel(), 'x')
        self.assertEqual(ax.get_ylabel(), 'y')
        self.assertEqual(max_y_point, (0.5, 0.6))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)