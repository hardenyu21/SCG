import numpy as np
import pandas as pd
import statistics

def task_func(rows, columns=['A', 'B', 'C', 'D', 'E', 'F'], seed=42):
    # Validate the number of rows
    if not isinstance(rows, int) or rows <= 0:
        raise ValueError("The 'rows' parameter must be a positive integer greater than 0.")
    
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Generate random numbers between 1 and 100
    data = np.random.randint(1, 101, size=(rows, len(columns)))
    
    # Create a DataFrame with the generated data
    df = pd.DataFrame(data, columns=columns)
    
    # Calculate the mean and median for each column
    stats_dict = {}
    for column in columns:
        mean_value = df[column].mean()
        median_value = df[column].median()
        stats_dict[column] = {
            'mean': mean_value,
            'median': median_value
        }
    
    return df, stats_dict

# Example usage:
# df, stats = task_func(10)
# print(df)
# print(stats)