import numpy as np
import random
from scipy import stats

def task_func(list_of_lists, size=5, seed=0):
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # Flatten the list of lists and fill empty lists with random integers
    all_values = []
    for lst in list_of_lists:
        if not lst:
            lst.extend(random.randint(0, 100) for _ in range(size))
        all_values.extend(lst)
    
    # Calculate mean
    mean_value = np.mean(all_values)
    
    # Calculate median
    median_value = np.median(all_values)
    
    # Calculate mode
    mode_result = stats.mode(all_values)
    mode_value = mode_result.mode[0] if mode_result.count[0] > 0 else None
    
    # Return the results in a dictionary
    return {
        'mean': mean_value,
        'median': median_value,
        'mode': mode_value
    }

# Example usage:
# list_of_lists = [[1, 2, 3], [], [4, 5, 6]]
# result = task_func(list_of_lists)
# print(result)