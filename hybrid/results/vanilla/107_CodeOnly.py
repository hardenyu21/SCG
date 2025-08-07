import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def task_func(df, n_clusters=3, random_state=0):
    # Check if the DataFrame is empty or lacks required columns
    if df.empty or not {'date', 'value'}.issubset(df.columns):
        raise ValueError("The DataFrame is empty or lacks required columns.")
    
    # Convert the 'date' column to ordinal
    df['date_ordinal'] = pd.to_datetime(df['date']).map(pd.Timestamp.toordinal)
    
    # Perform KMeans clustering on 'date_ordinal' and 'value' columns
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)
    df['cluster'] = kmeans.fit_predict(df[['date_ordinal', 'value']])
    
    # Plot the clusters
    fig, ax = plt.subplots()
    scatter = ax.scatter(df['date_ordinal'], df['value'], c=df['cluster'], cmap='viridis')
    
    # Add labels and title
    ax.set_xlabel('Date (ordinal)')
    ax.set_ylabel('Value')
    ax.set_title('KMeans Clustering of Value vs Date')
    
    # Add a legend
    legend1 = ax.legend(*scatter.legend_elements(), title="Clusters")
    ax.add_artist(legend1)
    
    # Show the plot
    plt.show()
    
    return ax