import numpy as np
from sklearn.cluster import KMeans

def task_func(data, n_clusters=2, random_state=0):
    # Extract the 2D coordinates from the data
    coordinates = np.array([(x, y) for _, x, y in data])
    
    # Initialize the KMeans model
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)
    
    # Fit the model to the coordinates and predict the cluster labels
    labels = kmeans.fit_predict(coordinates)
    
    return labels

# Example usage
data = [('T1', 1, 1), ('T2', 1, 1.1), ('T2', 1.1, 1), ('C1', 400, 400), ('C2', 401, 401), ('B1', 35, 35)]
labels = task_func(data, n_clusters=3, random_state=42)
print(labels)