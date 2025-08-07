import pickle
import os
import random
import string

def task_func(strings, filename=None):
    # Generate a unique filename if none is provided
    if filename is None:
        filename = f"random_strings_{os.getpid()}_{random.randint(1000, 9999)}.pkl"
    
    # Save the list of strings to a pickle file
    with open(filename, 'wb') as file:
        pickle.dump(strings, file)
    
    # Read the list of strings back from the pickle file
    with open(filename, 'rb') as file:
        loaded_strings = pickle.load(file)
    
    # Return the loaded list of strings
    return loaded_strings

# Example usage:
# random_strings = [''.join(random.choices(string.ascii_letters, k=10)) for _ in range(5)]
# loaded_strings = task_func(random_strings)
# print(loaded_strings)