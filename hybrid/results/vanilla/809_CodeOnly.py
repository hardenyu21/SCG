import numpy as np
from sklearn.cluster import KMeans

def task_func(data, n_clusters):
    # Initialize the KMeans model
    kmeans = KMeans(n_clusters=n_clusters, random_state=0)
    
    # Fit the model to the data
    kmeans.fit(data)
    
    # Get the cluster labels for each data point
    labels = kmeans.labels_
    
    # Create a dictionary to store the indices of data points in each cluster
    cluster_dict = {}
    for i, label in enumerate(labels):
        if label not in cluster_dict:
            cluster_dict[label] = []
        cluster_dict[label].append(i)
    
    # Convert the lists of indices to numpy arrays
    for label in cluster_dict:
        cluster_dict[label] = np.array(cluster_dict[label])
    
    return cluster_dict

# Example usage
data = np.array([[1, 1], [2, 2]])
cluster = task_func(data, 2)
cluster_list = list(cluster.values())
cluster_list.sort(key=lambda x: x[0])
print(cluster_list)  # Output: [array([0]), array([1])]