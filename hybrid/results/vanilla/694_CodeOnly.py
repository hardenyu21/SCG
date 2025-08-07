import itertools
import random

def task_func(t, n):
    # Generate all combinations of length n from the tuple t
    combinations = list(itertools.combinations(t, n))
    
    # Return a random combination from the list of combinations
    return random.choice(combinations)

# Example usage:
# t = (1, 2, 3, 4)
# n = 2
# print(task_func(t, n))