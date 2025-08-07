import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(column, data):
    # Check if the data list is empty
    if not data:
        # Return NaN for mean, min, and max if the data is empty
        return {
            'sum': 0,
            'mean': np.nan,
            'min': np.nan,
            'max': np.nan
        }, None

    # Convert the data list to a DataFrame
    df = pd.DataFrame(data)

    # Check if the specified column exists in the DataFrame
    if column not in df.columns:
        raise ValueError(f"Column '{column}' does not exist in the data.")

    # Calculate the statistics
    column_data = df[column]
    column_sum = column_data.sum()
    column_mean = column_data.mean()
    column_min = column_data.min()
    column_max = column_data.max()

    # Create a dictionary with the statistics
    stats = {
        'sum': column_sum,
        'mean': column_mean,
        'min': column_min,
        'max': column_max
    }

    # Create a pie chart using the Age column as labels
    fig, ax = plt.subplots()
    ax.pie(column_data, labels=df['Age'], autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Return the statistics and the Axes object
    return stats, ax