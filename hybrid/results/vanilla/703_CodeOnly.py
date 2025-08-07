import pandas as pd
from sklearn.cluster import DBSCAN

def task_func(data, cols):
    # Transform the data into a DataFrame
    df = pd.DataFrame(data, columns=cols)
    
    # Initialize the DBSCAN model with the specified parameters
    dbscan = DBSCAN(eps=3, min_samples=2)
    
    # Fit the model and predict the clusters
    df['Cluster'] = dbscan.fit_predict(df)
    
    return df