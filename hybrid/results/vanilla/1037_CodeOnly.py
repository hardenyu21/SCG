import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def task_func(s1, s2, n_clusters=3):
    # Check if s1 and s2 are pandas Series
    if not isinstance(s1, pd.Series) or not isinstance(s2, pd.Series):
        raise ValueError("s1 and s2 must be pandas Series")
    
    # Check if s1 and s2 have the same length
    if len(s1) != len(s2):
        raise ValueError("s1 and s2 must have the same length")
    
    # Combine the data points from s1 and s2
    data = pd.DataFrame({'s1': s1, 's2': s2})
    
    # Perform K-Means clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=0)
    kmeans.fit(data)
    labels = kmeans.labels_
    
    # Create a scatter plot
    fig, ax = plt.subplots()
    scatter = ax.scatter(data['s1'], data['s2'], c=labels, cmap='viridis', marker='o')
    
    # Add a legend
    legend1 = ax.legend(*scatter.legend_elements(), title="Clusters")
    ax.add_artist(legend1)
    
    # Set the plot title
    ax.set_title("K-Means Clustering")
    
    # Show the plot
    plt.show()
    
    # Return the cluster labels and the Axes object
    return labels, ax