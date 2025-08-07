import numpy as np
import itertools
import random
import statistics

def task_func(T1, RANGE=100):
    # Check if T1 is empty
    if not T1:
        raise statistics.StatisticsError("T1 is empty")
    
    # Convert elements in T1 to integers
    try:
        int_list = [int(x) for x in T1]
    except ValueError:
        raise ValueError("All elements in T1 must be convertible to integers")
    
    # Calculate the size of the list as the sum of the integers in T1
    list_size = sum(int_list)
    
    # Generate a list of random integers with the calculated size
    random_list = [random.randint(0, RANGE) for _ in range(list_size)]
    
    # Calculate the mean, median, and mode
    mean_value = statistics.mean(random_list)
    median_value = statistics.median(random_list)
    mode_value = statistics.mode(random_list)
    
    # Return the results as a tuple
    return (mean_value, median_value, mode_value)