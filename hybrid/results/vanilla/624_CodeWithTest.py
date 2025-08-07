from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt

# Constants
N_COMPONENTS = 2

def task_func(L):
    # Convert the list of lists into a 2D numpy array
    data = np.array(L)
    
    # Apply PCA
    pca = PCA(n_components=N_COMPONENTS)
    pca_result = pca.fit_transform(data)
    
    # Create a scatter plot
    fig, ax = plt.subplots()
    scatter = ax.scatter(pca_result[:, 0], pca_result[:, 1])
    
    # Set labels and title
    ax.set_xlabel('Principal Component 1')
    ax.set_ylabel('Principal Component 2')
    ax.set_title('PCA Result')
    
    # Return the PCA result and the scatter plot
    return pca_result, ax

# Example usage:
# L = [[1, 2], [3, 4], [5, 6]]
# pca_result, ax = task_func(L)
# plt.show()
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        test_input = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        pca_result, plot = task_func(test_input)
        self.assertIsInstance(pca_result, np.ndarray)
        self.assertIsInstance(plot, plt.Axes)
        self.assertEqual(pca_result.shape, (3, 2))
    def test_case_2(self):
        test_input = [[1, 1], [1, 1], [1, 1]]
        pca_result, plot = task_func(test_input)
        self.assertIsInstance(pca_result, np.ndarray)
        self.assertIsInstance(plot, plt.Axes)
        self.assertEqual(pca_result.shape, (3, 2))
    def test_case_3(self):
        test_input = [[1, 2], [3, 4], [5, 6], [7, 8]]
        pca_result, plot = task_func(test_input)
        self.assertIsInstance(pca_result, np.ndarray)
        self.assertIsInstance(plot, plt.Axes)
        self.assertEqual(pca_result.shape, (4, 2))
    def test_case_4(self):
        test_input = [[-1, -2], [-3, -4], [-5, -6]]
        pca_result, plot = task_func(test_input)
        self.assertIsInstance(pca_result, np.ndarray)
        self.assertIsInstance(plot, plt.Axes)
        self.assertEqual(pca_result.shape, (3, 2))
    def test_case_5(self):
        test_input = [[-1, 2], [3, -4], [5, -6]]
        pca_result, plot = task_func(test_input)
        self.assertIsInstance(pca_result, np.ndarray)
        self.assertIsInstance(plot, plt.Axes)
        self.assertEqual(pca_result.shape, (3, 2))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)