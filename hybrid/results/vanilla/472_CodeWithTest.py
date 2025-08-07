import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np

def task_func(myList, n_clusters):
    # Validate input
    if not isinstance(myList, list) or not all(isinstance(point, (list, tuple)) and len(point) == 2 for point in myList):
        raise ValueError("Input must be a list of 2D points (list of lists or tuples with two elements each).")
    if not isinstance(n_clusters, int) or n_clusters <= 0:
        raise ValueError("Number of clusters must be a positive integer.")
    
    # Convert list to numpy array
    data = np.array(myList)
    
    # Perform KMeans clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    kmeans.fit(data)
    labels = kmeans.labels_
    centers = kmeans.cluster_centers_
    
    # Plot the clusters
    fig, ax = plt.subplots()
    scatter = ax.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis', marker='o')
    ax.scatter(centers[:, 0], centers[:, 1], c='red', marker='x', s=100, label='Centroids')
    
    # Add legend and show plot
    ax.legend()
    plt.title('KMeans Clustering')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    
    return ax

# Example usage:
# ax = task_func([[1, 2], [1, 4], [1, 0],
#                 [10, 2], [10, 4], [10, 0]], 2)
# plt.show()
import unittest
import numpy as np
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def setUp(self):
        self.test_list = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
    def test_case_1(self):
        # Test single cluster
        myList = [[1, 1], [1, 1], [1, 1], [1, 1]]
        ax = task_func(myList, 1)
        self.assertEqual(len(set(ax.collections[0].get_array())), 1)
    def test_case_2(self):
        # Test arbitrary number of clusters
        myList = self.test_list
        for n in range(1, 6):
            ax = task_func(myList, n)
            self.assertEqual(len(set(ax.collections[0].get_array())), n)
    def test_case_3(self):
        # Test visualization
        myList = self.test_list
        ax = task_func(myList, 2)
        red_collection = next(
            coll
            for coll in ax.collections
            if (
                coll.get_facecolor()[0][0] == 1.0
                and coll.get_facecolor()[0][1] == 0.0
                and coll.get_facecolor()[0][2] == 0.0
            )
        )
        red_x_markers_count = len(red_collection.get_offsets())
        self.assertEqual(red_x_markers_count, 2)
    def test_case_4(self):
        # Test handling invalid inputs
        with self.assertRaises(ValueError):
            task_func([], 1)
        with self.assertRaises(ValueError):
            task_func([[1, 1], [2, 2]], 0)
        with self.assertRaises(ValueError):
            task_func(self.test_list, len(self.test_list) + 1)
    def test_case_5(self):
        # Test consistency across runs with built-in random seed
        myList = self.test_list
        ax1 = task_func(myList, 2)
        ax2 = task_func(myList, 2)
        colors1 = ax1.collections[0].get_array()
        colors2 = ax2.collections[0].get_array()
        self.assertTrue(all(c1 == c2 for c1, c2 in zip(colors1, colors2)))
    def tearDown(self):
        plt.close("all")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)