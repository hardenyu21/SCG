import numpy as np
import random

def task_func(length=10000, seed=0):
    if length < 0:
        raise ValueError("Length must be non-negative.")
    
    random.seed(seed)
    steps = [random.choice([-1, 1]) for _ in range(length)]
    walk = np.cumsum([0] + steps)
    
    return walk

# Example usage:
# walk = task_func(10)
# print(walk)