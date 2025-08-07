import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def task_func(array, features=None, seed=None):
    # Check if the array is empty or not 2-dimensional
    if array.size == 0 or array.ndim != 2:
        raise ValueError("The array must be non-empty and 2-dimensional.")
    
    # Check if features is provided and matches the number of columns
    if features is not None and len(features) != array.shape[1]:
        raise ValueError("The number of features must match the number of columns in the array.")
    
    # Set the random seed for reproducibility
    if seed is not None:
        np.random.seed(seed)
    
    # Shuffle the columns of the array
    shuffled_indices = np.random.permutation(array.shape[1])
    shuffled_array = array[:, shuffled_indices]
    
    # Prepare the feature labels
    if features is None:
        features = [str(i + 1) for i in range(array.shape[1])]
    else:
        features = [features[i] for i in shuffled_indices]
    
    # Create the heatmap
    plt.figure(figsize=(10, 8))
    ax = sns.heatmap(shuffled_array, xticklabels=features, yticklabels=False, cmap='viridis')
    plt.xlabel('Features')
    plt.title('Shuffled Column Heatmap')
    plt.show()
    
    return ax
import unittest
import numpy as np
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def setUp(self):
        np.random.seed(0)
        self.array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
        self.expected_labels = ["1", "2", "3", "4", "5"]
    def test_default_features(self):
        """Test heatmap with default features."""
        ax = task_func(self.array)
        xticklabels = [tick.get_text() for tick in ax.get_xticklabels()]
        self.assertEqual(xticklabels, self.expected_labels)
        self.assertTrue(len(ax.collections), 1)
    def test_custom_features(self):
        """Test heatmap with custom features."""
        custom_labels = ["A", "B", "C", "D", "E"]
        ax = task_func(self.array, features=custom_labels)
        xticklabels = [tick.get_text() for tick in ax.get_xticklabels()]
        self.assertEqual(xticklabels, custom_labels)
        self.assertTrue(len(ax.collections), 1)
    def test_features_mismatch(self):
        """Test for error when features list does not match array dimensions."""
        with self.assertRaises(ValueError):
            task_func(self.array, features=["A", "B"])
    def test_seed_reproducibility(self):
        """Test if seeding makes shuffling reproducible."""
        ax1 = task_func(self.array, seed=42)
        ax2 = task_func(self.array, seed=42)
        heatmap_data1 = ax1.collections[0].get_array().data
        heatmap_data2 = ax2.collections[0].get_array().data
        np.testing.assert_array_equal(heatmap_data1, heatmap_data2)
    def test_empty_array(self):
        """Test for handling an empty array."""
        with self.assertRaises(ValueError):
            task_func(np.array([]))
    def tearDown(self):
        """Cleanup plot figures after each test."""
        plt.close("all")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)