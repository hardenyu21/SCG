import pandas as pd
import numpy as np

def task_func(column, data):
    # Check if the data is empty
    if data.empty:
        return {
            'sum': 0,
            'mean': np.nan,
            'min': np.nan,
            'max': np.nan
        }
    
    # Check if the specified column exists in the data
    if column not in data.columns:
        raise ValueError("The specified column name is not valid.")
    
    # Calculate the required statistics
    column_data = data[column]
    result = {
        'sum': column_data.sum(),
        'mean': column_data.mean(),
        'min': column_data.min(),
        'max': column_data.max()
    }
    
    return result