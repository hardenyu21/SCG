from typing import List, Union
import numpy as np
import scipy.fft

def task_func(data: List[Union[int, str]], repetitions: int = 1):
    # Check if the data is empty or repetitions is less than or equal to 0
    if not data or repetitions <= 0:
        return {'mode': np.array([]), 'count': np.array([])}
    
    # Repeat the data the specified number of times
    repeated_data = data * repetitions
    
    # Calculate the mode(s) and their count(s)
    unique_elements, counts = np.unique(repeated_data, return_counts=True)
    max_count = np.max(counts)
    modes = unique_elements[counts == max_count]
    
    # Sort the modes in ascending order
    modes_sorted = np.sort(modes)
    
    # Calculate the Fast Fourier Transform of the repeated data
    fft_result = scipy.fft.fft(repeated_data)
    
    # Return the result as a dictionary
    return {
        'mode': modes_sorted,
        'count': np.full_like(modes_sorted, max_count)
    }

# Example usage:
# result = task_func([1, 2, 2, 3, 3, 3], 2)
# print(result)