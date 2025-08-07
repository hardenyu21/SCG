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