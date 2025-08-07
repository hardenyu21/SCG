import pandas as pd
import numpy as np
import itertools

def task_func(T1, row_num=50, seed=None):
    # Flatten the tuple and convert elements to integers
    flat_list = list(itertools.chain.from_iterable(T1))
    int_list = [int(x) for x in flat_list]
    
    # Calculate the number of columns based on the sum of integers
    num_columns = sum(int_list)
    
    # Set the random seed for reproducibility
    if seed is not None:
        np.random.seed(seed)
    
    # Generate random numbers and create a DataFrame
    data = np.random.randint(0, 100, size=(row_num, num_columns))
    column_names = [f'Col_{i+1}' for i in range(num_columns)]
    df = pd.DataFrame(data, columns=column_names)
    
    return df