import numpy as np
import datetime

def task_func(arr):
    # Ensure the input is a numpy array
    arr = np.array(arr)
    
    # Function to reverse the order of words in a string
    def reverse_words(s):
        return ' '.join(s.split()[::-1])
    
    # Apply the reverse_words function to each element in the array
    reversed_arr = np.vectorize(reverse_words)(arr)
    
    return reversed_arr

# Example usage:
# arr = np.array(["hello.world", "this.is.a.test", "numpy.array.reverse"])
# print(task_func(arr))