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