from scipy import stats
import matplotlib.pyplot as plt

def task_func(data_dict, data_keys):
    # Extract the data series from the dictionary using the provided keys
    series1 = data_dict[data_keys[0]]
    series2 = data_dict[data_keys[1]]
    
    # Calculate the correlation coefficient
    correlation_coefficient, _ = stats.pearsonr(series1, series2)
    
    # Create a scatter plot
    fig, ax = plt.subplots()
    ax.scatter(series1, series2)
    ax.set_xlabel(data_keys[0])
    ax.set_ylabel(data_keys[1])
    ax.set_title(f'Scatter Plot of {data_keys[0]} vs {data_keys[1]}')
    
    # Return the correlation coefficient and the Axes object
    return correlation_coefficient, ax

# Example usage:
# data_dict = {'A': [1, 2, 3, 4, 5], 'B': [5, 4, 3, 2, 1]}
# data_keys = ['A', 'B']
# correlation, ax = task_func(data_dict, data_keys)
# plt.show()
import unittest
import numpy as np
import doctest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        data_dict = {'X': [1, 2, 3, 4, 5], 'Y': [2, 3, 5, 7, 8]}
        data_keys = ['X', 'Y']
        correlation, plot = task_func(data_dict, data_keys)
        self.assertAlmostEqual(correlation, 0.9923, places=4)
        self.assertTrue(isinstance(plot, plt.Axes))
        
    def test_case_2(self):
        data_dict = {'A': [5, 4, 3, 2, 1], 'B': [1, 2, 3, 4, 5]}
        data_keys = ['A', 'B']
        correlation, plot = task_func(data_dict, data_keys)
        self.assertAlmostEqual(correlation, -1.0, places=4)
        self.assertTrue(isinstance(plot, plt.Axes))
        
    def test_case_3(self):
        data_dict = {'X': [1, 1, 1, 1, 1], 'Y': [1, 1, 1, 1, 1]}
        data_keys = ['X', 'Y']
        correlation, plot = task_func(data_dict, data_keys)
        self.assertTrue(np.isnan(correlation))
        self.assertTrue(isinstance(plot, plt.Axes))
        
    def test_case_4(self):
        data_dict = {'X': [1, 2, 3, 4, 5], 'Y': [1, 4, 9, 16, 25]}
        data_keys = ['X', 'Y']
        correlation, plot = task_func(data_dict, data_keys)
        self.assertAlmostEqual(correlation, 0.9811, places=4)
        self.assertTrue(isinstance(plot, plt.Axes))
        
    def test_case_5(self):
        data_dict = {'X': [1, 3, 5, 7, 9], 'Y': [2, 6, 10, 14, 18]}
        data_keys = ['X', 'Y']
        correlation, plot = task_func(data_dict, data_keys)
        self.assertAlmostEqual(correlation, 1.0, places=4)
        self.assertTrue(isinstance(plot, plt.Axes))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)