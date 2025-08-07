import json
import numpy as np
import pandas as pd

def task_func(df):
    # Transform the 'IntCol' column by applying a logarithm (base 10)
    df['IntCol'] = np.log10(df['IntCol'])
    
    # Convert the transformed 'IntCol' column to a list
    int_col_list = df['IntCol'].tolist()
    
    # Write the list to a JSON file
    with open('IntCol.json', 'w') as json_file:
        json.dump(int_col_list, json_file)
    
    # Return the transformed DataFrame
    return df