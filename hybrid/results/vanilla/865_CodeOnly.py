import pandas as pd
import numpy as np
from scipy.stats import zscore
from sklearn.preprocessing import MinMaxScaler

def task_func(data):
    # Unpack the data into separate lists
    items = [item for item, _, _ in data]
    counts = [count for _, count, _ in data]
    weights = [weight for _, _, weight in data]
    
    # Convert counts and weights to numpy arrays for processing
    counts_array = np.array(counts)
    weights_array = np.array(weights)
    
    # Normalize counts using z-score normalization
    normalized_counts = zscore(counts_array)
    
    # Normalize weights using min-max scaling
    scaler = MinMaxScaler()
    normalized_weights = scaler.fit_transform(weights_array.reshape(-1, 1)).flatten()
    
    # Create a DataFrame with the results
    df = pd.DataFrame({
        'Item': items,
        'Normalized Count': normalized_counts,
        'Normalized Weight': normalized_weights
    })
    
    return df