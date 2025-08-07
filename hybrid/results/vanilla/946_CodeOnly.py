import numpy as np
import pandas as pd
import random

def task_func(rows=3, cols=2, min_val=0, max_val=100, seed=0):
    # Set the random seed for reproducibility
    random.seed(seed)
    np.random.seed(seed)
    
    # Generate a matrix of random integers within the specified range
    matrix = np.random.randint(min_val, max_val + 1, size=(rows, cols))
    
    # Convert the matrix into a pandas DataFrame
    df = pd.DataFrame(matrix)
    
    return df

# Example usage:
# df = task_func(4, 3, 10, 50, 42)
# print(df)