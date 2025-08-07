import numpy as np
import pandas as pd
from sklearn.decomposition import PCA

def task_func(array, seed=None):
    # Check if the input array is 2D
    if array.ndim != 2:
        raise ValueError("Input array must be 2D.")
    
    # Check if the array is empty or has no features
    if array.size == 0 or array.shape[1] == 0:
        return pd.DataFrame(columns=['PC1', 'PC2'])
    
    # Shuffle the columns of the array randomly
    if seed is not None:
        np.random.seed(seed)
    shuffled_indices = np.random.permutation(array.shape[1])
    shuffled_array = array[:, shuffled_indices]
    
    # Determine the number of components for PCA
    n_components = min(2, shuffled_array.shape[1])
    
    # Perform PCA
    pca = PCA(n_components=n_components)
    principal_components = pca.fit_transform(shuffled_array)
    
    # Create a DataFrame with the principal components
    if n_components == 1:
        # If only one component, add a column of zeros for PC2
        principal_components = np.column_stack((principal_components, np.zeros(principal_components.shape[0])))
    
    df = pd.DataFrame(principal_components, columns=['PC1', 'PC2'])
    
    return df
import unittest
import numpy as np
class TestCases(unittest.TestCase):
    def setUp(self):
        self.array2x5 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
        self.array5x1 = np.array([[1], [2], [3], [4], [5]])
    def test_with_empty_array(self):
        """Test handling of an empty array."""
        array = np.empty((0, 0))
        df = task_func(array, seed=42)
        self.assertTrue(df.empty, "The returned DataFrame should be empty.")
        self.assertTrue(
            (df.columns == ["PC1", "PC2"]).all(),
            "Column names should be 'PC1' and 'PC2' even for an empty DataFrame.",
        )
    def test_with_2x5_array(self):
        """Test PCA on a 2x5 array with shuffled columns."""
        df = task_func(self.array2x5, seed=42)
        self.assertEqual(df.shape, (2, 2), "DataFrame shape should be (2, 2).")
        self.assertTrue(
            (df.columns == ["PC1", "PC2"]).all(),
            "Column names should be 'PC1' and 'PC2'.",
        )
    def test_with_5x1_array(self):
        """Test PCA on a 5x1 array."""
        df = task_func(self.array5x1, seed=0)
        self.assertEqual(
            df.shape, (5, 1), "DataFrame shape should be (5, 1) for a single component."
        )
        self.assertTrue(
            (df.columns == ["PC1"]).all(),
            "Column name should be 'PC1' for a single component.",
        )
    def test_invalid_input(self):
        """Test handling of invalid input."""
        with self.assertRaises(ValueError):
            task_func(np.array([1, 2, 3]), seed=42)
    def test_reproducibility(self):
        """Test if the function is reproducible with the same seed."""
        df1 = task_func(self.array2x5, seed=42)
        df2 = task_func(self.array2x5, seed=42)
        pd.testing.assert_frame_equal(
            df1, df2, "Results should be identical when using the same seed."
        )
    def test_pca_correctness(self):
        """
        Test PCA correctness by ensuring that the variance is captured correctly
        in the principal components.
        """
        # Creating a simple array where variance is higher in one dimension
        # This dataset is designed so that the first principal component should
        # capture the majority of the variance.
        array = np.array(
            [
                [1, 2, 3, 4, 5],
                [1, 2, 3, 4, 5],
                [1, 2, 3, 4, 5],
                [1, 2, 3, 4, 5],
                [10, 10, 10, 10, 10],
            ]
        )  # Increased variance in the last row
        df = task_func(array, seed=0)
        # The PCA should be able to capture the variance in the first principal component
        # significantly more than in the second, if applicable.
        # Asserting that the first PC values are not all the same,
        # which indicates it captured the variance.
        self.assertFalse(
            df["PC1"].std() == 0,
            "PCA should capture variance along the first principal component.",
        )


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)