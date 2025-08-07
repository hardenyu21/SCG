import random
import numpy as np

def task_func(LETTERS):
    # Create a dictionary with specified letters as keys and lists of random integers as values
    random_dict = {letter: [random.randint(0, 100) for _ in range(random.randint(1, 10))] for letter in LETTERS}
    
    # Calculate the mean of integers for each key
    mean_dict = {letter: np.mean(values) for letter, values in random_dict.items()}
    
    return mean_dict

# Example usage:
# LETTERS = ['A', 'B', 'C']
# print(task_func(LETTERS))