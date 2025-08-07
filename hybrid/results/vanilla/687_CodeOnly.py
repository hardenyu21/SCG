import numpy as np
from scipy.stats import mode

def task_func(list_of_lists):
    # Merge the list of lists into a single list
    merged_list = [item for sublist in list_of_lists for item in sublist]
    
    # Convert the merged list to a numpy array
    merged_array = np.array(merged_list)
    
    # Find the mode of the merged array
    mode_result = mode(merged_array)
    
    # Extract the mode value and its count
    mode_value = mode_result.mode[0]
    mode_count = mode_result.count[0]
    
    # Return the results as specified
    return (mode_value, mode_count), mode_value, mode_count

# Example usage:
list_of_lists = [[1, 2, 2, 3], [2, 3, 3, 4], [3, 4, 4, 4]]
result = task_func(list_of_lists)
print(result)