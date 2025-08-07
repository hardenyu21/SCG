import random
import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt
from typing import List, Tuple

def task_func(length, range_limit=100, seed=0) -> Tuple[plt.Axes, List[int]]:
    if range_limit <= 1:
        raise ValueError("range_limit must be greater than 1.")
    
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # Generate a list of random numbers
    random_numbers = [random.randint(0, range_limit) for _ in range(length)]
    
    # Sort the list of random numbers
    random_numbers.sort()
    
    # Create a histogram using seaborn
    plt.figure(figsize=(8, 6))
    ax = sns.histplot(random_numbers, kde=False)
    
    # Return the axes object and the list of random numbers
    return ax, random_numbers

# Example usage:
# ax, numbers = task_func(100, range_limit=50, seed=42)
# plt.show()