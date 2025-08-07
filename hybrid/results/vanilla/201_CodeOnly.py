import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(df, column, value):
    # Check if the column exists in the DataFrame
    if column not in df.columns:
        raise ValueError(f"Column '{column}' does not exist in the DataFrame.")
    
    # Check if the value is a number
    if not isinstance(value, (int, float)):
        raise ValueError("The value must be a number.")
    
    # Calculate the average of the column
    average = df[column].mean()
    
    # Find values greater than the average
    values_greater_than_average = df[column][df[column] > average].values
    
    # Count the number of values greater than the given value
    count_greater_than_value = (df[column] > value).sum()
    
    # Plot a histogram of the column
    fig, ax = plt.subplots()
    ax.hist(df[column], bins=10, alpha=0.7, color='blue', edgecolor='black')
    ax.set_title(f'Histogram of {column}')
    ax.set_xlabel(column)
    ax.set_ylabel('Frequency')
    
    # Return the results as a tuple
    return values_greater_than_average, count_greater_than_value, ax

# Example usage:
# df = pd.DataFrame({'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})
# result = task_func(df, 'A', 5)
# print(result)