import numpy as np
from scipy.stats import ttest_1samp
import matplotlib.pyplot as plt

# Constants
ALPHA = 0.05

def task_func(data_matrix):
    # Calculate the mean of each row
    row_means = np.mean(data_matrix, axis=1)
    
    # Calculate the population mean
    population_mean = np.mean(data_matrix)
    
    # Initialize a list to store indices of significant means
    significant_indices = []
    
    # Perform t-test for each row mean against the population mean
    for i, row_mean in enumerate(row_means):
        t_stat, p_value = ttest_1samp(data_matrix[i], population_mean)
        if p_value < ALPHA:
            significant_indices.append(i)
    
    # Plotting
    fig, ax = plt.subplots()
    
    # Plot the mean of each row
    ax.plot(range(len(row_means)), row_means, color='red', label='Means')
    
    # Plot the significant means
    if significant_indices:
        ax.plot(significant_indices, row_means[significant_indices], 'bo', label='Significant Means')
    
    # Plot the population mean as a horizontal line
    ax.axhline(y=population_mean, color='green', linestyle='--', label='Population Mean')
    
    # Add labels and legend
    ax.set_xlabel('Row Index')
    ax.set_ylabel('Mean Value')
    ax.legend()
    
    # Show the plot
    plt.show()
    
    return significant_indices, ax

# Example usage
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
indices, ax = task_func(data)
print(indices)
import unittest
class TestCases(unittest.TestCase):
    """Test cases for the task_func function."""
    def test_case_1(self):
        data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self._validate_function(data)
    def test_case_2(self):
        data = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
        self._validate_function(data)
    def test_case_3(self):
        data = np.array([[3, 5, 7, 1000], [200, 5, 7, 1], [1, 9, 14, 700]])
        self._validate_function(data)
    def test_case_4(self):
        data = np.array(
            [
                [1, 2, 3, 4, 5, 4, 3, 2, 1],
            ]
        )
        self._validate_function(data)
    def test_case_5(self):
        data = np.array([[1], [1], [1]])
        self._validate_function(data)
    def _validate_function(self, data):
        indices, ax = task_func(data)
        self.assertIsInstance(indices, list)
        lines = ax.get_lines()
        self.assertEqual(len(lines), 3)
        self.assertEqual(lines[0].get_color(), "r")
        self.assertEqual(lines[0].get_label(), "Means")
        self.assertEqual(lines[1].get_color(), "b")
        self.assertEqual(lines[1].get_label(), "Significant Means")
        self.assertEqual(lines[2].get_color(), "g")
        self.assertEqual(lines[2].get_label(), "Population Mean")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)