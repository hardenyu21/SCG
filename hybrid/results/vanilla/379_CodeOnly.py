import pandas as pd
import numpy as np

# Constants
COLUMNS = ['Column1', 'Column2', 'Column3', 'Column4', 'Column5']

def task_func(length):
    # Generate random data
    data = np.random.rand(length, len(COLUMNS))
    
    # Create a DataFrame
    df = pd.DataFrame(data, columns=COLUMNS)
    
    # Record the data (for demonstration, we'll just print it)
    print(df)
    
    # Return the DataFrame
    return df

# Example usage
df = task_func(10)