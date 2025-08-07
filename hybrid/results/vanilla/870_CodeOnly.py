import pandas as pd
import numpy as np
import itertools

def task_func(data_list=[('a', 1, 2.1), ('b', 2, 3.2), ('c', 3, 4.3), ('d', 4, 5.4), ('e', 5, 6.5)]):
    if not data_list:
        return pd.DataFrame(columns=['Mean Value'])

    # Determine the maximum length of tuples in the list
    max_length = max(len(t) for t in data_list)

    # Initialize a list to store means for each position
    means = []

    # Iterate over each position
    for i in range(max_length):
        # Collect all numeric values at the current position
        values = []
        for item in data_list:
            if i < len(item) and isinstance(item[i], (int, float)):
                values.append(item[i])
        
        # Calculate the mean if there are any numeric values
        if values:
            mean_value = np.mean(values)
        else:
            mean_value = np.nan
        
        # Append the mean to the list
        means.append(mean_value)

    # Create a DataFrame with the mean values
    df = pd.DataFrame({'Mean Value': means}, index=[f'Position {i}' for i in range(max_length)])
    
    return df

# Example usage
data = [('a', '1', 2.1), ('b', 21, 'c'), (12, 3, 4.3), (['d'], 4, 5.4), ('e', 5, 6.5)]
df = task_func(data)
print(df)