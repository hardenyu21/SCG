import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def task_func(x, y, labels):
    # Combine x and y into a single dataset
    data = np.column_stack((x, y))
    
    # Perform PCA
    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(data)
    
    # Create a scatter plot of the principal components
    fig, ax = plt.subplots()
    scatter = ax.scatter(principal_components[:, 0], principal_components[:, 1], c='blue', alpha=0.5)
    
    # Annotate each point with its label
    for i, label in enumerate(labels):
        ax.annotate(label, (principal_components[i, 0], principal_components[i, 1]))
    
    # Set plot labels
    ax.set_xlabel('Principal Component 1')
    ax.set_ylabel('Principal Component 2')
    ax.set_title('PCA of x and y values')
    
    # Return the figure object
    return fig
import unittest
class TestCases(unittest.TestCase):
    def setUp(self):
        # Generate sample data for testing
        self.x_data = [
            np.array([1, 2, 3, 4]),
            np.array([5, 6, 7, 8]),
            np.array([9, 10, 11, 12]),
            np.array([13, 14, 15, 16]),
            np.array([17, 18, 19, 20])
        ]
        
        self.y_data = [
            np.array([21, 22, 23, 24]),
            np.array([25, 26, 27, 28]),
            np.array([29, 30, 31, 32]),
            np.array([33, 34, 35, 36]),
            np.array([37, 38, 39, 40])
        ]
        
        self.labels = ['H₂O', 'O₂', 'CO₂', 'N₂', 'Ar']
    def test_case_1(self):
        fig = task_func(self.x_data, self.y_data, self.labels)
        # Check if returned object is a matplotlib figure
        self.assertIsInstance(fig, plt.Figure)
    def test_case_2(self):
        # Testing with different data lengths
        x_data = [np.array([1, 2, 3]), np.array([4, 5, 6]), np.array([7, 8, 9])]
        y_data = [np.array([10, 11, 12]), np.array([13, 14, 15]), np.array([16, 17, 18])]
        fig = task_func(x_data, y_data, self.labels[:3])
        self.assertIsInstance(fig, plt.Figure)
    def test_case_3(self):
        # Testing with data of length 2 (to avoid PCA error)
        x_data = [np.array([1, 2]), np.array([4, 5]), np.array([7, 8])]
        y_data = [np.array([10, 11]), np.array([13, 14]), np.array([16, 17])]
        fig = task_func(x_data, y_data, self.labels[:3])
        self.assertIsInstance(fig, plt.Figure)
        
    def test_case_4(self):
        # Testing with longer data
        x_data = [np.array(range(10)), np.array(range(10, 20)), np.array(range(20, 30))]
        y_data = [np.array(range(30, 40)), np.array(range(40, 50)), np.array(range(50, 60))]
        fig = task_func(x_data, y_data, self.labels[:3])
        self.assertIsInstance(fig, plt.Figure)
        
    def test_case_5(self):
        # Testing with random data
        x_data = [np.random.randn(10) for _ in range(3)]
        y_data = [np.random.randn(10) for _ in range(3)]
        fig = task_func(x_data, y_data, self.labels[:3])
        self.assertIsInstance(fig, plt.Figure)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)