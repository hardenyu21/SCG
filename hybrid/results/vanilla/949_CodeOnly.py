import numpy as np
import pandas as pd

def task_func(rows, columns, seed=None):
    """
    Generates a DataFrame with random values within a specified range.

    Parameters:
    - rows (int): Number of rows in the DataFrame.
    - columns (int): Number of columns in the DataFrame.
    - seed (int, optional): Random seed for reproducibility. Defaults to None.

    Returns:
    - DataFrame: A Pandas DataFrame containing the generated random values.
    """
    if seed is not None:
        np.random.seed(seed)
    
    # Generate random values between 0 and 1
    random_values = np.random.rand(rows, columns)
    
    # Create a DataFrame from the random values
    df = pd.DataFrame(random_values)
    
    return df

# Example usage:
# df = task_func(5, 3, seed=42)
# print(df)