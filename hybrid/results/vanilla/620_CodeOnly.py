import numpy as np
import pandas as pd

# Constants
RANGE = (1, 100)

def task_func(L):
    # Calculate the number of rows and columns by multiplying pairs of integers
    rows = 1
    cols = 1
    for sublist in L:
        if len(sublist) == 2:
            rows *= sublist[0]
            cols *= sublist[1]
    
    # Generate random integers within the specified range
    data = np.random.randint(RANGE[0], RANGE[1], size=(rows, cols))
    
    # Create a DataFrame from the generated data
    df = pd.DataFrame(data)
    
    return df

# Example usage:
# L = [[2, 3], [4, 5]]
# df = task_func(L)
# print(df)