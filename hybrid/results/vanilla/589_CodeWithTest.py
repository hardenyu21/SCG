import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

# Constants for configuration
RANGE = 100
SIZE = 1000
CLUSTERS = 5

def task_func():
    # Generate random 2D points within the specified range
    data_points = np.random.rand(SIZE, 2) * RANGE
    
    # Apply KMeans clustering
    kmeans = KMeans(n_clusters=CLUSTERS, random_state=0)
    kmeans.fit(data_points)
    
    # Get the cluster labels and centroids
    labels = kmeans.labels_
    centroids = kmeans.cluster_centers_
    
    # Plot the clustered points
    plt.figure(figsize=(8, 6))
    for i in range(CLUSTERS):
        # Plot points belonging to the current cluster
        plt.scatter(data_points[labels == i, 0], data_points[labels == i, 1], label=f'Cluster {i+1}')
    
    # Plot the centroids
    plt.scatter(centroids[:, 0], centroids[:, 1], s=300, c='red', marker='X', label='Centroids')
    
    # Add plot details
    plt.title('KMeans Clustering')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    # Return the data points and the fitted KMeans model
    return data_points, kmeans

# Call the function to execute the task
task_func()
import unittest
class TestCases(unittest.TestCase):
    def test_data_size(self):
        """Ensure the generated data has the correct size."""
        data, _ = task_func()
        self.assertEqual(data.shape, (SIZE, 2))
    def test_cluster_centers_shape(self):
        """Check the shape of the cluster centers array."""
        _, kmeans = task_func()
        self.assertEqual(kmeans.cluster_centers_.shape, (CLUSTERS, 2))
    def test_fitted_model(self):
        """Verify the model is a KMeans instance and is fitted."""
        _, kmeans = task_func()
        self.assertIsInstance(kmeans, KMeans)
        self.assertTrue(hasattr(kmeans, 'labels_'))
    def test_data_range(self):
        """Ensure that generated data points fall within the specified range."""
        data, _ = task_func()
        self.assertTrue((data >= 0).all() and (data <= RANGE).all())
    def test_cluster_labels(self):
        """Verify that cluster labels are assigned to each data point."""
        _, kmeans = task_func()
        self.assertEqual(len(kmeans.labels_), SIZE)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)