import collections
import string
import random

def task_func(length, seed=0):
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # Generate a random string of the given length using ASCII letters
    random_string = ''.join(random.choices(string.ascii_letters, k=length))
    
    # Calculate the frequency of each character in the generated string
    frequency = collections.Counter(random_string)
    
    return dict(frequency)

# Example usage:
# print(task_func(10))