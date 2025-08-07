from matplotlib import pyplot as plt
from sklearn.decomposition import PCA
import numpy as np

def task_func(arr):
    # Sum the rows of the 2D array
    row_sums = np.sum(arr, axis=1).reshape(-1, 1)
    
    # Perform PCA on the row sums
    pca = PCA(n_components=1)
    pca.fit(row_sums)
    
    # Get the explained variance ratio
    explained_variance_ratio = pca.explained_variance_ratio_
    
    # Plot the explained variance ratio
    fig, ax = plt.subplots()
    ax.bar(range(1, len(explained_variance_ratio) + 1), explained_variance_ratio, alpha=0.7, align='center')
    ax.set_title("Explained Variance Ratio of Principal Components")
    ax.set_xlabel("Principal Component")
    ax.set_ylabel("Explained Variance Ratio")
    
    # Show the plot
    plt.show()
    
    return ax
import unittest
import numpy as np
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt
class TestCases(unittest.TestCase):
    """Tests for function task_func."""
    def test_basic_functionality(self):
        """Test basic functionality of task_func."""
        arr = np.array([[i + j for i in range(3)] for j in range(5)])
        result = task_func(arr)
        self.assertIsInstance(result, plt.Axes)
    def test_plot_title_verification(self):
        """Test that the plot title is correct."""
        arr = np.array([[i + j for i in range(3)] for j in range(5)])
        result = task_func(arr)
        self.assertEqual(
            result.get_title(), "Explained Variance Ratio of Principal Components"
        )
    def test_bar_count_verification(self):
        """Test that the number of bars is correct."""
        arr = np.array([[i + j for i in range(3)] for j in range(5)])
        result = task_func(arr)
        n_components = min(2, arr.sum(axis=1).reshape(-1, 1).shape[1])
        self.assertEqual(len(result.patches), n_components)
    def test_variance_ratios_verification(self):
        """Test that the variance ratios are correct."""
        arr = np.array([[i + j for i in range(3)] for j in range(5)])
        row_sums = arr.sum(axis=1)
        n_components = min(2, row_sums.reshape(-1, 1).shape[1])
        pca = PCA(n_components=n_components)
        pca.fit(row_sums.reshape(-1, 1))
        result = task_func(arr)
        for bar, variance_ratio in zip(result.patches, pca.explained_variance_ratio_):
            self.assertAlmostEqual(bar.get_height(), variance_ratio)
    def test_empty_input(self):
        """Test that an empty input raises a ValueError."""
        arr = np.array([])
        with self.assertRaises(ValueError):
            task_func(arr)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)