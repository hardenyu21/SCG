import numpy as np
from scipy.stats import iqr

def task_func(L):
    # Flatten the nested list
    flat_list = [item for sublist in L for item in sublist]
    
    # Calculate the interquartile range
    iqr_value = iqr(flat_list)
    
    return iqr_value