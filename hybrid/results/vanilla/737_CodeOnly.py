import numpy as np
import math

def task_func(L):
    # Flatten the nested list
    flat_list = [item for sublist in L for item in sublist]
    
    # Calculate the median using numpy
    median = np.median(flat_list)
    
    return median