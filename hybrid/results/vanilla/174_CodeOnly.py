import pandas as pd
import numpy as np

def task_func(data, key, min_value, max_value):
    # Check if the input data is a pandas DataFrame
    if not isinstance(data, pd.DataFrame):
        raise TypeError("The input data must be a pandas DataFrame.")
    
    # Generate random values within the specified range
    random_values = np.random.uniform(min_value, max_value, size=len(data))
    
    # Add the new column to the DataFrame
    data[key] = random_values
    
    # Return the updated DataFrame
    return data