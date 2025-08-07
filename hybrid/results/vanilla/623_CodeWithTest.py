from itertools import chain
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def task_func(L):
    # Flatten the list of lists into a single list of integers
    flat_list = list(chain.from_iterable(L))
    
    # Convert the list of integers into a numpy array with a single feature
    data = np.array(flat_list).reshape(-1, 1)
    
    # Apply KMeans clustering
    kmeans = KMeans(n_clusters=3, random_state=0)  # You can adjust the number of clusters
    kmeans.fit(data)
    labels = kmeans.labels_
    
    # Create a scatter plot
    fig, ax = plt.subplots()
    ax.scatter(data, np.zeros_like(data), c=labels, cmap='viridis', marker='o')
    
    # Add labels and title
    ax.set_xlabel('Data Points')
    ax.set_yticks([])  # Hide y-axis ticks as they are not meaningful
    ax.set_title('KMeans Clustering')
    
    # Return the Axes object
    return ax

# Example usage:
# ax = task_func([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# plt.show()
import unittest
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def test_case_1(self):
        ax = task_func([[1, 2, 3], [50, 60, 70], [100, 110, 120]])
        self.assertIsInstance(ax, plt.Axes)
    def test_case_2(self):
        ax = task_func([[1, 5], [2, 6], [3, 7]])
        self.assertIsInstance(ax, plt.Axes)
    def test_case_3(self):
        ax = task_func([[10, 20, 30, 40], [15, 25, 35, 45]])
        self.assertIsInstance(ax, plt.Axes)
    def test_case_4(self):
        ax = task_func([[1000, 2000], [3000, 4000], [5000, 6000]])
        self.assertIsInstance(ax, plt.Axes)
    def test_case_5(self):
        ax = task_func([[-1, -2, -3], [-50, -60, -70], [-100, -110, -120]])
        self.assertIsInstance(ax, plt.Axes)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)