import pandas as pd
import numpy as np

def task_func(d):
    # Check if the input is a list of dictionaries
    if not isinstance(d, list) or not all(isinstance(item, dict) for item in d):
        raise ValueError("Input must be a list of dictionaries.")
    
    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(d)
    
    # Check if the DataFrame contains the required keys
    required_keys = {'x', 'y', 'z'}
    if not required_keys.issubset(df.columns):
        raise ValueError("Input dictionaries must contain the keys 'x', 'y', and 'z'.")
    
    # Calculate statistics for each key
    statistics = {}
    for key in required_keys:
        stats = {
            'mean': df[key].mean(),
            'sum': df[key].sum(),
            'max': df[key].max(),
            'min': df[key].min(),
            'std': df[key].std()
        }
        statistics[key] = stats
    
    return statistics