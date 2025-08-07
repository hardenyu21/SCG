import numpy as np
import pandas as pd

def task_func(n_rows, remove_cols, columns=['A', 'B', 'C', 'D', 'E'], random_seed=None):
    # Set the random seed for reproducibility
    if random_seed is not None:
        np.random.seed(random_seed)
    
    # Generate random integer values between 0 and 100
    data = np.random.randint(0, 101, size=(n_rows, len(columns)))
    
    # Create a DataFrame with the generated data and specified columns
    df = pd.DataFrame(data, columns=columns)
    
    # Remove columns based on the provided indexes
    df = df.drop(df.columns[remove_cols], axis=1)
    
    return df

# Example usage
df = task_func(3, [1, 3], columns=['test', 'rem1', 'apple', 'remove'], random_seed=12)
print(df)