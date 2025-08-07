import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def task_func(elements, seed=0):
    # Validate input
    if not isinstance(elements, int) or elements <= 0:
        raise ValueError("elements must be a positive integer.")
    
    # Set random seed for reproducibility
    np.random.seed(seed)
    
    # Generate random steps of -1 or 1
    steps = np.random.choice([-1, 1], size=elements)
    
    # Compute the random walk
    random_walk = np.cumsum(steps)
    
    # Calculate descriptive statistics
    descriptive_stats = {
        'count': len(random_walk),
        'mean': np.mean(random_walk),
        'std': np.std(random_walk),
        'min': np.min(random_walk),
        '5th_percentile': np.percentile(random_walk, 5),
        '25th_percentile': np.percentile(random_walk, 25),
        'median': np.median(random_walk),
        '75th_percentile': np.percentile(random_walk, 75),
        '95th_percentile': np.percentile(random_walk, 95),
        'max': np.max(random_walk)
    }
    
    # Plot the random walk
    fig, ax = plt.subplots()
    ax.plot(random_walk)
    ax.set_title('Random Walk')
    ax.set_xlabel('Step')
    ax.set_ylabel('Position')
    
    # Return the descriptive statistics and the Axes object
    return descriptive_stats, ax

# Example usage:
# stats, ax = task_func(100)
# plt.show()
# print(stats)