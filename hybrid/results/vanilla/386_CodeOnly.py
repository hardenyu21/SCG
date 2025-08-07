import numpy as np
import pandas as pd

# Constants
COLUMNS = ['Column1', 'Column2', 'Column3', 'Column4', 'Column5']

def task_func(length, min_value=0, max_value=100):
    # Generate random data within the specified range
    data = np.random.uniform(min_value, max_value, size=(length, len(COLUMNS)))
    
    # Create a DataFrame with the generated data
    df = pd.DataFrame(data, columns=COLUMNS)
    
    # Calculate the cumulative distribution function (CDF) for each column
    cdf_df = df.rank(method='average', pct=True)
    
    return cdf_df

# Example usage
length = 10
cdf_df = task_func(length)
print(cdf_df)