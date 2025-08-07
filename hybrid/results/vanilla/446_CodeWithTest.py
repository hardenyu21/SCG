import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

def task_func(n_samples=100, centers=3, n_features=2, random_seed=42):
    # Generate isotropic Gaussian blobs for clustering
    X, y = make_blobs(n_samples=n_samples, centers=centers, n_features=n_features, random_state=random_seed)
    
    # Create a scatter plot of the blobs
    fig, ax = plt.subplots()
    scatter = ax.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', marker='o', edgecolor='k', s=50)
    
    # Add a legend
    legend1 = ax.legend(*scatter.legend_elements(), title="Classes")
    ax.add_artist(legend1)
    
    # Set plot title and labels
    ax.set_title('Isotropic Gaussian Blobs')
    ax.set_xlabel('Feature 1')
    ax.set_ylabel('Feature 2')
    
    # Show the plot
    plt.show()
    
    # Return the data and the Axes object
    return X, y, ax

# Example usage
X, y, ax = task_func()
import unittest
import matplotlib
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test default case
        n_samples, n_features, centers = 100, 2, 3
        X, y, ax = task_func()
        self.assertEqual(X.shape, (n_samples, n_features))
        self.assertEqual(y.shape, (n_samples,))
        self.assertIsInstance(ax, matplotlib.axes.Axes)
        self.assertEqual(len(set(y)), centers)
    def test_case_2(self):
        # Test n_samples
        for n_samples in [1, 50, 100]:
            X, y, _ = task_func(n_samples=n_samples)
            self.assertEqual(X.shape[0], n_samples)
            self.assertEqual(y.shape[0], n_samples)
    def test_case_3(self):
        # Test centers
        for centers in [1, 50, 100]:
            _, y, _ = task_func(centers=centers)
        self.assertEqual(len(set(y)), centers)
    def test_case_4(self):
        # Test n_features
        for n_features in [2, 50, 100]:
            X, y, _ = task_func(n_features=n_features)
            self.assertEqual(X.shape[1], n_features)
    def test_case_5(self):
        # Test random seed
        X1, y1, _ = task_func(n_samples=100, centers=3, n_features=2, random_seed=42)
        X2, y2, _ = task_func(n_samples=100, centers=3, n_features=2, random_seed=42)
        self.assertTrue((X1 == X2).all())
        self.assertTrue((y1 == y2).all())
    def test_case_6(self):
        # Test with the minimum possible values that are still valid
        n_samples, n_features, centers = 1, 2, 1
        X, y, ax = task_func(
            n_samples=1, centers=centers, n_features=n_features, random_seed=0
        )
        self.assertEqual(X.shape, (n_samples, n_features))
        self.assertEqual(y.shape, (n_samples,))
        self.assertEqual(len(set(y)), centers)
        self.assertIsInstance(ax, matplotlib.axes.Axes)
    def test_case_7(self):
        # Example of handling an expected failure due to invalid input
        with self.assertRaises(ValueError):
            task_func(n_samples=-100)
        with self.assertRaises(ValueError):
            task_func(centers=-10)
        with self.assertRaises(Exception):
            task_func(n_features=0)
        with self.assertRaises(ValueError):
            task_func(random_seed="invalid")
    def tearDown(self):
        plt.close("all")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)