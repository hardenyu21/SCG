import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(P, T):
    """
    Calculate the product of a matrix 'P' and a 3D tensor 'T' using numpy and visualize the results as a heatmap.

    Parameters:
    P (numpy.ndarray): A 2D numpy array (matrix).
    T (numpy.ndarray): A 3D numpy array (tensor).

    Returns:
    numpy.ndarray: Resultant product after matrix-tensor multiplication.
    matplotlib.axes.Axes: Axes object displaying the heatmap of the 2D result.
    """
    # Ensure P is a 2D array and T is a 3D array
    if P.ndim != 2:
        raise ValueError("P must be a 2D numpy array (matrix).")
    if T.ndim != 3:
        raise ValueError("T must be a 3D numpy array (tensor).")
    
    # Check if the dimensions are compatible for multiplication
    if P.shape[1] != T.shape[0]:
        raise ValueError("The number of columns in P must match the first dimension of T.")
    
    # Perform the matrix-tensor multiplication
    # The result will be a 3D array where each 2D slice is the product of P and a 2D slice of T
    result = np.tensordot(P, T, axes=(1, 0))
    
    # Sum over the third dimension to get a 2D result
    result_2d = np.sum(result, axis=2)
    
    # Plot the heatmap
    plt.figure(figsize=(8, 6))
    ax = sns.heatmap(result_2d, annot=True, fmt=".2f", cmap="viridis")
    plt.title("Heatmap of the Resultant 2D Array")
    plt.xlabel("Columns")
    plt.ylabel("Rows")
    plt.show()
    
    return result_2d, ax

# Example usage:
# P = np.array([[1, 2], [3, 4]])
# T = np.random.rand(2, 3, 4)
# result_2d, ax = task_func(P, T)
import unittest
import numpy as np
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def setUp(self):
        np.random.seed(0)
        self.test_P = np.array([[6, 2, 7], [1, 1, 8]])
        self.test_P_zeros = np.zeros((2, 3))
        self.test_T = np.array(
            [
                [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                [[2, 3, 4], [5, 6, 7], [8, 9, 10]],
                [[3, 4, 5], [6, 7, 8], [9, 10, 11]],
            ]
        )
    def test_case_1(self):
        # Test return types
        product, heatmap = task_func(self.test_P, self.test_T)
        self.assertIsInstance(product, np.ndarray)
        self.assertIsInstance(heatmap, plt.Axes)
    def test_case_2(self):
        # Test output correctness
        product, _ = task_func(self.test_P, self.test_T)
        expected_product = np.tensordot(self.test_P, self.test_T, axes=[1, 0])
        self.assertTrue(np.allclose(product, expected_product))
    def test_case_3(self):
        # Test output correctness with zeros
        product, _ = task_func(self.test_P_zeros, self.test_T)
        self.assertTrue(np.all(product == 0))
    def test_case_4(self):
        # Test return shape
        product, _ = task_func(self.test_P, self.test_T)
        expected_shape = (2, 3, 3)
        self.assertEqual(product.shape, expected_shape, "Output shape is incorrect")
    def test_case_5(self):
        # Test handling invalid input types
        with self.assertRaises(TypeError):
            task_func([1, 2], [2, 1])
    def test_case_6(self):
        # Test handling invalid shape
        P = np.array([[1, 2], [3, 4]])
        T = np.random.rand(3, 3, 3)
        with self.assertRaises(ValueError):
            task_func(P, T)
    def tearDown(self):
        plt.close("all")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)