import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(column, data):
    # Validate that the data list is not empty
    if not data:
        raise ValueError("The data list is empty.")
    
    # Convert the data list to a DataFrame
    df = pd.DataFrame(data)
    
    # Validate that the specified column is valid
    if column not in df.columns:
        raise KeyError(f"The specified column '{column}' is not valid.")
    
    # Validate that numeric values for steps, calories burned, and distance walked are non-negative
    numeric_columns = ['steps', 'calories burned', 'distance walked']
    for col in numeric_columns:
        if col in df.columns and (df[col] < 0).any():
            raise ValueError(f"Negative values found in the column '{col}'.")
    
    # Calculate the sum, mean, min, max of the specified column
    column_data = df[column]
    column_stats = {
        'sum': column_data.sum(),
        'mean': column_data.mean(),
        'min': column_data.min(),
        'max': column_data.max()
    }
    
    # Plot the line chart
    fig, ax = plt.subplots()
    ax.plot(df['Date'], column_data, marker='o')
    ax.set_title(f'Line Chart of {column}')
    ax.set_xlabel('Date')
    ax.set_ylabel(column)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Return the statistics and the Axes object
    return column_stats, ax