import pandas as pd
from sklearn.cluster import KMeans

def task_func(x_list, y_list, n_clusters=2, random_state=0):
    # Create a DataFrame from the input lists
    data = pd.DataFrame({'x': x_list, 'y': y_list})
    
    # Initialize the KMeans model
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)
    
    # Fit the model to the data
    kmeans.fit(data)
    
    # Get the labels and centroids
    labels = kmeans.labels_
    centroids = kmeans.cluster_centers_
    
    # Return the labels and centroids as a tuple
    return (labels, centroids)

# Example usage:
# x_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# y_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# labels, centroids = task_func(x_list, y_list, n_clusters=2)
# print("Labels:", labels)
# print("Centroids:", centroids)