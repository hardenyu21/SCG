import pandas as pd
import numpy as np

def task_func(rows=100, columns=3):
    # Generate random alphabets
    random_alphabets = np.random.choice(list('abcdefghijklmnopqrstuvwxyz'), size=(rows, columns))
    
    # Create column names
    column_names = list('abcdefghijklmnopqrstuvwxyz')[:columns]
    
    # Create DataFrame
    df = pd.DataFrame(random_alphabets, columns=column_names)
    
    return df

# Example usage:
# df = task_func(5, 4)
# print(df)