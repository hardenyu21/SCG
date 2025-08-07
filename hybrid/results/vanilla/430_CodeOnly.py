from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def task_func(df1, df2, column1="feature1", column2="feature2"):
    # Merge datasets on the id column
    merged_df = pd.merge(df1, df2, on='id')
    
    # Extract the feature columns for clustering
    X = merged_df[[column1, column2]].values
    
    # Perform KMeans clustering
    kmeans = KMeans(n_clusters=2, n_init=10, random_state=42)
    kmeans.fit(X)
    
    # Get the cluster labels
    labels = kmeans.labels_
    
    # Create a scatterplot
    fig, ax = plt.subplots()
    scatter = ax.scatter(merged_df[column1], merged_df[column2], c=labels, cmap='viridis', marker='o')
    
    # Add labels and title
    ax.set_xlabel(column1)
    ax.set_ylabel(column2)
    ax.set_title('KMeans Clustering')
    
    # Add a legend
    legend1 = ax.legend(*scatter.legend_elements(), title="Clusters")
    ax.add_artist(legend1)
    
    # Return the cluster labels and the Axes object
    return labels, ax

# Example usage:
# df1 = pd.DataFrame({'id': [1, 2, 3], 'feature1': [1.0, 2.0, 3.0]})
# df2 = pd.DataFrame({'id': [1, 2, 3], 'feature2': [4.0, 5.0, 6.0]})
# labels, ax = task_func(df1, df2)
# plt.show()