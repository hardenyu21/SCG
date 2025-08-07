import numpy as np
from scipy import stats

def task_func(L):
    # Flatten the nested list
    flat_list = [item for sublist in L for item in sublist]
    
    # Calculate the mode
    mode_result = stats.mode(flat_list)
    
    # Extract the mode value
    mode = mode_result.mode[0]
    
    return mode