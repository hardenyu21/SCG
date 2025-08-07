import numpy as np
import random

# Constants
ELEMENTS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

def task_func(l=None):
    # If no list is provided, generate a random list of elements
    if l is None:
        l = random.sample(ELEMENTS, len(ELEMENTS))
    
    # Convert the list to a numpy array
    arr = np.array(l)
    
    # Move the first 3 elements to the end of the array
    arr = np.concatenate((arr[3:], arr[:3]))
    
    return arr

# Example usage
if __name__ == "__main__":
    # Example with a predefined list
    example_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    result = task_func(example_list)
    print("Processed array with predefined list:", result)
    
    # Example with a random list
    random_result = task_func()
    print("Processed array with random list:", random_result)