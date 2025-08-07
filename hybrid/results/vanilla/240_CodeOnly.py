import pandas as pd
from random import uniform

def task_func(n_data_points=1000, min_value=0.0, max_value=10.0, column_name='Value'):
    # Generate random floating-point numbers
    data = [uniform(min_value, max_value) for _ in range(n_data_points)]
    
    # Truncate each value to 3 decimal places
    truncated_data = [round(num, 3) for num in data]
    
    # Create a DataFrame with the specified column name
    df = pd.DataFrame(truncated_data, columns=[column_name])
    
    return df

# Example usage:
# df = task_func()
# print(df)