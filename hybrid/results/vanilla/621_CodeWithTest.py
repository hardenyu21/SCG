from itertools import chain
import numpy as np
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

def task_func(L):
    # Flatten the list of lists into a single list of integers
    flat_list = list(chain.from_iterable(L))
    
    # Convert the list to a numpy array and reshape for scikit-learn
    data = np.array(flat_list).reshape(-1, 1)
    
    # Standardize the data
    scaler = StandardScaler()
    standardized_data = scaler.fit_transform(data).flatten()
    
    # Plot the standardized values
    fig, ax = plt.subplots()
    ax.plot(standardized_data, marker='o', linestyle='-')
    ax.set_title('Standardized Values')
    ax.set_xlabel('Index')
    ax.set_ylabel('Standardized Value')
    
    # Show the plot
    plt.show()
    
    return ax

# Example usage:
# L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# ax = task_func(L)
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        ax = task_func([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.lines[0].get_ydata()), 9)
    def test_case_2(self):
        ax = task_func([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]])
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.lines[0].get_ydata()), 9)
    def test_case_3(self):
        ax = task_func([[1, -2, 3], [-4, 5, -6], [7, -8, 9]])
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.lines[0].get_ydata()), 9)
    def test_case_4(self):
        ax = task_func([[1, 2, 3, 4, 5]])
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.lines[0].get_ydata()), 5)
    def test_case_5(self):
        ax = task_func([[1, 2], [3, 4, 5, 6], [7]])
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.lines[0].get_ydata()), 7)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)