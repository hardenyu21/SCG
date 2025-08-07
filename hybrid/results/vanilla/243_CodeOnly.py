import pandas as pd
import random

# Constants
N_DATA_POINTS = 10000
MIN_VALUE = 0.0
MAX_VALUE = 10.0

def task_func(n_data_points=N_DATA_POINTS):
    if n_data_points == 0:
        return pd.DataFrame(columns=['Value'])
    
    # Generate random floating-point numbers
    random_values = [random.uniform(MIN_VALUE, MAX_VALUE) for _ in range(n_data_points)]
    
    # Truncate each value to 3 decimal places
    truncated_values = [round(value, 3) for value in random_values]
    
    # Create a DataFrame
    df = pd.DataFrame(truncated_values, columns=['Value'])
    
    return df