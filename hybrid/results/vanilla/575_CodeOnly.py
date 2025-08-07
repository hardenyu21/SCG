from random import shuffle
import pandas as pd
import numpy as np

# Constants
def task_func(l, n_groups=5):
    # Shuffle the list
    shuffle(l)
    
    # Determine the number of columns for the DataFrame
    num_columns = len(l)
    
    # Create a DataFrame from the shuffled list
    df = pd.DataFrame([l], columns=[f'col_{i+1}' for i in range(num_columns)])
    
    # Function to move the first n_groups elements to the end of the row
    def shift_elements(row):
        return np.concatenate((row[n_groups:], row[:n_groups]))
    
    # Apply the shift_elements function to each row in the DataFrame
    df = df.apply(shift_elements, axis=1, result_type='expand')
    
    # Rename columns to maintain consistency
    df.columns = [f'col_{i+1}' for i in range(num_columns)]
    
    return df

# Example usage:
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(task_func(l, n_groups=3))