from collections import Counter
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd

def task_func(df, n_clusters=3, random_state=None, n_init=10):
    # Identify duplicate points
    duplicates = df.duplicated(keep=False)
    duplicate_counts = Counter(df[duplicates].values.tolist())
    
    # Remove duplicates to get unique points
    unique_df = df.drop_duplicates()
    
    # Perform KMeans clustering on unique points
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state, n_init=n_init)
    unique_df['cluster'] = kmeans.fit_predict(unique_df)
    
    # Plot the clustered data
    fig, ax = plt.subplots()
    scatter = ax.scatter(unique_df.iloc[:, 0], unique_df.iloc[:, 1], c=unique_df['cluster'], cmap='viridis')
    legend1 = ax.legend(*scatter.legend_elements(), title="Clusters")
    ax.add_artist(legend1)
    ax.set_title('KMeans Clustering of Unique Points')
    
    return duplicate_counts, unique_df, ax

# Example usage:
# df = pd.DataFrame([[1, 2], [1, 2], [3, 4], [5, 6], [3, 4], [7, 8]], columns=['x', 'y'])
# duplicate_counts, clustered_df, ax = task_func(df)
# plt.show()