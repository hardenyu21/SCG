import pandas as pd
import numpy as np

DEFAULT_COLUMNS = ['Element', 'Count']

def task_func(elements, include_index=False):
    # Calculate the character count for each element
    counts = [len(element) for element in elements]
    
    # Create a dictionary to hold the data
    data = {
        'Element': elements,
        'Count': counts
    }
    
    # If index is to be included, add an 'Index' column
    if include_index:
        data['Index'] = np.arange(len(elements))
        columns = ['Index'] + DEFAULT_COLUMNS
    else:
        columns = DEFAULT_COLUMNS
    
    # Create the DataFrame
    df = pd.DataFrame(data, columns=columns)
    
    return df

# Example usage:
# elements = ["apple", "banana", "cherry"]
# df = task_func(elements, include_index=True)
# print(df)