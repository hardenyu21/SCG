import numpy as np
import matplotlib.pyplot as plt

def task_func(arr):
    # Calculate the unique values and their counts
    unique, counts = np.unique(arr, return_counts=True)
    
    # Determine if the distribution is uniform
    uniform_distribution = np.all(counts == counts[0])
    
    # Create a histogram
    fig, ax = plt.subplots()
    ax.hist(arr, bins=np.arange(len(unique) + 1) - 0.5, edgecolor='black')
    
    # Set labels and title
    ax.set_xlabel('Unique Values')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram of Array Distribution')
    
    # Display the histogram
    plt.show()
    
    return uniform_distribution, ax

# Example usage:
# arr = np.array([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
# uniform, ax = task_func(arr)
# print("Is the distribution uniform?", uniform)
import numpy as np
import unittest
class TestCases(unittest.TestCase):
    """Test cases for task_func"""
    def test_uniform_distribution(self):
        """Test uniform distribution."""
        arr = np.array(["A", "A", "B", "B"])
        uniform, _ = task_func(arr)
        self.assertTrue(uniform)
    def test_non_uniform_distribution(self):
        """Test non-uniform distribution."""
        arr = np.array(["A", "A", "B", "B", "B", "C", "C", "C", "C", "D", "E", "E"])
        uniform, _ = task_func(arr)
        self.assertFalse(uniform)
    def test_single_value(self):
        """Test single value."""
        arr = np.array(["A", "A", "A", "A"])
        uniform, _ = task_func(arr)
        self.assertTrue(uniform)
    def test_multiple_equal_values(self):
        """Test multiple equal values."""
        arr = np.array(["A", "A", "B", "B", "C", "C", "D", "D"])
        uniform, _ = task_func(arr)
        self.assertTrue(uniform)
    def test_varying_values(self):
        """Test varying values."""
        arr = np.array(["A", "B", "B", "C", "C", "C", "D", "D", "D", "D"])
        uniform, _ = task_func(arr)
        self.assertFalse(uniform)
    def tearDown(self):
        plt.close()


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)