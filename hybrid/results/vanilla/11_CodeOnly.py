import numpy as np
import itertools
import random

def task_func(T1, max_value=100):
    # Convert string representations of integers to actual integers
    int_list = [int(num) for tup in T1 for num in tup]
    
    # Calculate the total size of the list of random integers
    total_size = sum(int_list)
    
    # Generate a list of random integers with the calculated size
    random_list = [random.randint(0, max_value) for _ in range(total_size)]
    
    # Calculate the 25th, 50th, and 75th percentiles
    p25 = np.percentile(random_list, 25)
    p50 = np.percentile(random_list, 50)
    p75 = np.percentile(random_list, 75)
    
    # Return the percentiles as a tuple
    return (p25, p50, p75)

# Example usage:
# T1 = (("1", "2"), ("3", "4"))
# print(task_func(T1))