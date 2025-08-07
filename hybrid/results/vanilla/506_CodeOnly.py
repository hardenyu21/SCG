import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(column, data):
    # Convert the list of weather observations into a DataFrame
    df = pd.DataFrame(data, columns=['date', 'temperature', 'humidity', 'wind_speed', 'precipitation'])
    
    # Check if the DataFrame is empty
    if df.empty:
        return {
            'sum': np.nan,
            'mean': np.nan,
            'min': np.inf,
            'max': -np.inf,
            'plot': None
        }
    
    # Calculate the sum, mean, min, and max of the specified column
    sum_value = df[column].sum()
    mean_value = df[column].mean()
    min_value = df[column].min()
    max_value = df[column].max()
    
    # Generate a histogram plot of the specified column
    fig, ax = plt.subplots()
    plot = ax.hist(df[column], bins=10, edgecolor='black')
    
    # Return the results as a dictionary
    return {
        'sum': sum_value,
        'mean': mean_value,
        'min': min_value,
        'max': max_value,
        'plot': plot
    }