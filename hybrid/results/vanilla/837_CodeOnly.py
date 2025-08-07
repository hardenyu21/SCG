import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(n_rows, scale_cols, columns=['A', 'B', 'C', 'D', 'E'], random_seed=None):
    # Set the random seed for reproducibility
    if random_seed is not None:
        np.random.seed(random_seed)
    
    # Generate random values for the DataFrame
    data = np.random.randint(0, 100, size=(n_rows, len(columns)))
    
    # Create the DataFrame
    df = pd.DataFrame(data, columns=columns)
    
    # Check if there are any columns to scale
    if scale_cols:
        # Initialize the StandardScaler
        scaler = StandardScaler()
        
        # Scale the specified columns
        df.iloc[:, scale_cols] = scaler.fit_transform(df.iloc[:, scale_cols])
    
    return df

# Example usage
df = task_func(5, [1, 2, 3], random_seed=12)
print(df)