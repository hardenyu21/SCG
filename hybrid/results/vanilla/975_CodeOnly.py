import numpy as np
import pandas as pd

def task_func(rows, columns=["A", "B", "C", "D", "E"], seed=0) -> pd.DataFrame:
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Generate random values in the range [0, 1) with the specified number of rows and columns
    data = np.random.rand(rows, len(columns))
    
    # Create a DataFrame with the generated data and the specified columns
    df = pd.DataFrame(data, columns=columns)
    
    # Shuffle the columns
    shuffled_columns = np.random.permutation(columns)
    
    # Return the DataFrame with shuffled columns
    return df[shuffled_columns]

# Example usage:
# df = task_func(5)
# print(df)