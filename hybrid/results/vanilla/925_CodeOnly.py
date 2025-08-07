import pandas as pd
import numpy as np

def task_func(data_size=1000, column_names=['A', 'B', 'C', 'D', 'E'], seed=0):
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Generate a DataFrame with random integers between 1 and 100
    df = pd.DataFrame(np.random.randint(1, 101, size=(data_size, len(column_names))), columns=column_names)
    
    # Replace all values less than 10 with -1
    df[df < 10] = -1
    
    return df

# Example usage:
# df = task_func()
# print(df)