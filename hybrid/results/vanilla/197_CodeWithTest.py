import heapq
import math
import matplotlib.pyplot as plt

def task_func(l1, l2, N=10):
    # Calculate the absolute differences between the respective elements of l1 and l2
    differences = [abs(a - b) for a, b in zip(l1, l2)]
    
    # Find the N largest differences
    largest_differences = heapq.nlargest(N, differences)
    
    # Square the differences
    squared_differences = [diff ** 2 for diff in largest_differences]
    
    # Take the square root of the squared differences
    sqrt_differences = [math.sqrt(diff) for diff in squared_differences]
    
    # Plot the values
    fig, ax = plt.subplots()
    ax.plot(sqrt_differences, marker='o')
    ax.set_title('N Largest Differences')
    ax.set_xlabel('Index')
    ax.set_ylabel('Square Root of Squared Difference')
    
    # Return the Axes object
    return ax

# Example usage:
# l1 = [1, 2, 3, 4, 5]
# l2 = [5, 4, 3, 2, 1]
# ax = task_func(l1, l2, N=3)
# plt.show()
import unittest
import doctest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        l1 = [99, 86, 90, 70, 86, 95, 56, 98, 80, 81]
        l2 = [21, 11, 21, 1, 26, 40, 4, 50, 34, 37]
        ax = task_func(l1, l2)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.lines[0].get_ydata()), 10)
    def test_case_2(self):
        l1 = [10, 20, 30, 40, 50]
        l2 = [1, 2, 3, 4, 5]
        ax = task_func(l1, l2, 3)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.lines[0].get_ydata()), 3)
    def test_case_3(self):
        l1 = [0, 10, 20, 30, 40, 50]
        l2 = [0, 0, 0, 0, 0, 0]
        ax = task_func(l1, l2)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.lines[0].get_ydata()), 6)
    def test_case_4(self):
        l1 = [1, 2, 3, 4, 5]
        l2 = [5, 4, 3, 2, 1]
        ax = task_func(l1, l2)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.lines[0].get_ydata()), 5)
    def test_case_5(self):
        l1 = [0, 0, 0, 0, 0]
        l2 = [0, 0, 0, 0, 0]
        ax = task_func(l1, l2)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.lines[0].get_ydata()), 5)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)