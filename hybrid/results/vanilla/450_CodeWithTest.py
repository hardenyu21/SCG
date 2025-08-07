from scipy.spatial.distance import cdist
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

def task_func(n_samples=200, centers=4, plot_path=None, random_seed=None):
    # Generate synthetic 2D dataset
    X, y = make_blobs(n_samples=n_samples, centers=centers, random_state=random_seed)
    
    # Calculate the Euclidean distance between individual samples
    distances = cdist(X, X, 'euclidean')
    
    # Plot the dataset
    fig, ax = plt.subplots()
    scatter = ax.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', marker='o', edgecolor='k')
    legend1 = ax.legend(*scatter.legend_elements(), title="Classes")
    ax.add_artist(legend1)
    ax.set_xlabel('Feature 1')
    ax.set_ylabel('Feature 2')
    ax.set_title('Synthetic 2D Dataset')
    
    # Save or show the plot
    if plot_path:
        plt.savefig(plot_path)
        plt.close(fig)
        return distances, None
    else:
        return distances, ax

# Example usage:
# distances, ax = task_func(n_samples=200, centers=4, plot_path=None, random_seed=42)
# plt.show()  # Uncomment to display the plot if plot_path is None
import unittest
import tempfile
import os
import numpy as np
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def setUp(self):
        self.seed = 42
        self.temp_dir = tempfile.TemporaryDirectory()
    def test_case_1(self):
        # Default parameters
        distances, plot = task_func()
        self.assertEqual(distances.shape, (200, 200))
        self.assertEqual(len(plot.collections[0].get_offsets()), 200)
        self.assertEqual(len(set(plot.collections[0].get_array())), 4)
    def test_case_2(self):
        # Custom parameters
        n_samples, centers = 50, 5
        distances, plot = task_func(
            random_seed=self.seed, n_samples=n_samples, centers=centers
        )
        self.assertEqual(distances.shape, (n_samples, n_samples))
        self.assertEqual(len(plot.collections[0].get_offsets()), n_samples)
        self.assertEqual(len(set(plot.collections[0].get_array())), centers)
    def test_case_3(self):
        # Saving the plot to a path
        plot_path = os.path.join(self.temp_dir.name, "test_plot.png")
        distances, plot = task_func(random_seed=self.seed, plot_path=plot_path)
        self.assertEqual(distances.shape, (200, 200))
        self.assertTrue(os.path.exists(plot_path))
        self.assertIsNone(plot)
    def test_case_4(self):
        # Test reproducibility with the same seed
        distances1, _ = task_func(random_seed=self.seed)
        distances2, _ = task_func(random_seed=self.seed)
        np.testing.assert_array_equal(distances1, distances2)
        # Test different outputs with different seeds
        distances3, _ = task_func(random_seed=43)
        with self.assertRaises(AssertionError):
            np.testing.assert_array_equal(distances1, distances3)
    def test_case_5(self):
        # Test negative parameters for n_samples
        with self.assertRaises(ValueError):
            task_func(n_samples=-100, random_seed=self.seed)
    def test_case_6(self):
        # Test non-integer inputs for n_samples
        with self.assertRaises(TypeError):
            task_func(n_samples=200.5, random_seed=self.seed)
    def tearDown(self):
        plt.close("all")
        self.temp_dir.cleanup()


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)