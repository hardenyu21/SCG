import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from matplotlib.collections import PathCollection

def task_func(data, n_clusters=3):
    # Validate input
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input 'data' must be a pandas DataFrame.")
    if not isinstance(n_clusters, int) or n_clusters <= 1:
        raise ValueError("Input 'n_clusters' must be an integer greater than 1.")
    
    # Perform K-means clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(data)
    labels = kmeans.labels_
    centroids = kmeans.cluster_centers_
    
    # Create scatter plot
    fig, ax = plt.subplots()
    scatter = ax.scatter(data.iloc[:, 0], data.iloc[:, 1], c=labels, cmap='viridis', marker='o', edgecolor='k', s=50)
    
    # Plot centroids
    ax.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='x', s=200, label='Centroids')
    
    # Add legend and labels
    ax.legend()
    ax.set_xlabel(data.columns[0])
    ax.set_ylabel(data.columns[1])
    ax.set_title('K-means Clustering')
    
    # Return the cluster labels and the Axes object
    return labels, ax

# Example usage:
# df = pd.DataFrame({
#     'feature1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#     'feature2': [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# })
# labels, ax = task_func(df, n_clusters=3)
# plt.show()