import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def task_func(data, n_components=2, random_state=None):
    # Initialize PCA with the specified number of components
    pca = PCA(n_components=n_components, random_state=random_state)
    
    # Fit and transform the data
    transformed_data = pca.fit_transform(data)
    
    # Create a scatter plot
    fig, ax = plt.subplots()
    
    if n_components == 1:
        # For 1D data, plot along the X-axis with Y-values set to zero
        ax.scatter(transformed_data, np.zeros_like(transformed_data), alpha=0.7)
        ax.set_xlabel('Principal Component 1')
        ax.set_yticks([])  # Hide y-ticks for 1D plot
    else:
        # For 2D or more data, plot the first two principal components
        ax.scatter(transformed_data[:, 0], transformed_data[:, 1], alpha=0.7)
        ax.set_xlabel('Principal Component 1')
        ax.set_ylabel('Principal Component 2')
    
    # Set plot title
    ax.set_title('PCA Visualization')
    
    # Return the transformed data and the Axes object
    return {
        "transformed_data": transformed_data,
        "ax": ax
    }
import unittest
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def setUp(self):
        self.seed = 42
        self.n = 100
        self.n_dims = 5
        self.n_components = 2
        self.data = np.random.RandomState(self.seed).random((self.n, self.n_dims))
    def assert_pca_correctness(self, data, results, n_components, random_state):
        """Helper method to assert PCA correctness"""
        # 1. Variance explained
        pca = PCA(n_components=n_components, random_state=random_state)
        pca.fit(data)
        explained_variance_ratio = pca.explained_variance_ratio_
        if data.shape[1] == 1:
            # For one-dimensional data, the explained variance ratio should be 1
            self.assertAlmostEqual(explained_variance_ratio[0], 1.0, delta=1e-2)
        else:
            cov_matrix = np.cov(data, rowvar=False)
            eigenvalues = np.linalg.eigvals(cov_matrix)
            sorted_eigenvalues = np.sort(eigenvalues)[::-1][:n_components]
            normalized_eigenvalues = sorted_eigenvalues / sum(eigenvalues)
            self.assertTrue(
                np.allclose(explained_variance_ratio, normalized_eigenvalues, atol=1e-1)
            )
        # 2. Orthogonality
        for i in range(n_components):
            for j in range(i + 1, n_components):
                dot_product = np.dot(
                    results["transformed_data"][:, i], results["transformed_data"][:, j]
                )
                self.assertAlmostEqual(dot_product, 0, delta=1e-2)
    def test_case_1(self):
        # Test with default settings
        results = task_func(self.data, random_state=self.seed)
        self.assertEqual(results["transformed_data"].shape, (self.n, self.n_components))
        x_data = results["ax"].collections[0].get_offsets()[:, 0]
        y_data = results["ax"].collections[0].get_offsets()[:, 1]
        self.assertTrue(np.array_equal(x_data, results["transformed_data"][:, 0]))
        self.assertTrue(np.array_equal(y_data, results["transformed_data"][:, 1]))
        self.assert_pca_correctness(self.data, results, self.n_components, self.seed)
    def test_case_2(self):
        # Test n_components
        for n_components in [1, 2, min(self.data.shape)]:
            results = task_func(self.data, n_components=n_components, random_state=42)
            self.assertEqual(results["transformed_data"].shape[1], n_components)
            self.assert_pca_correctness(self.data, results, n_components, self.seed)
    def test_case_3(self):
        # Test when one of the features has zero variance
        data = self.data.copy()
        data[:, 1] = 0  # Second feature has zero variance
        results = task_func(data, n_components=2, random_state=self.seed)
        self.assertEqual(results["transformed_data"].shape, (100, 2))
        self.assert_pca_correctness(data, results, 2, self.seed)
    def test_case_4(self):
        # Test with n_components greater than min(n_samples, n_features)
        data = np.random.RandomState(self.seed).randn(10, 2)
        with self.assertRaises(ValueError):
            task_func(data, n_components=3, random_state=self.seed)
    def test_case_5(self):
        # Test with a single sample
        data = np.random.RandomState(self.seed).randn(1, self.n_dims)
        with self.assertRaises(ValueError):
            task_func(data)
    def test_case_6(self):
        # Edge case - test when dataset contains NaN
        data = self.data.copy()
        data[0, 0] = np.nan  # Introduce a NaN value
        with self.assertRaises(ValueError):
            task_func(data, n_components=2, random_state=self.seed)
    def test_case_7(self):
        # Edge case - test when dataset contains infinite values
        data = self.data.copy()
        data[0, 0] = np.inf  # Introduce an infinite value
        with self.assertRaises(ValueError):
            task_func(data, n_components=2, random_state=self.seed)
    def tearDown(self):
        plt.close("all")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)