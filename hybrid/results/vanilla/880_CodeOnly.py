import pandas as pd
from sklearn.cluster import KMeans

def task_func(data, n_clusters=3, seed=None):
    # Check if the DataFrame contains only numeric data
    if not all(data.dtypes.apply(lambda x: pd.api.types.is_numeric_dtype(x))):
        raise ValueError("The DataFrame contains non-numeric entries.")
    
    # Initialize the KMeans model
    kmeans = KMeans(n_clusters=n_clusters, n_init=10, random_state=seed)
    
    # Fit the model to the data
    kmeans.fit(data)
    
    # Get the cluster labels
    labels = kmeans.labels_
    
    # Return the labels and the fitted model
    return labels, kmeans