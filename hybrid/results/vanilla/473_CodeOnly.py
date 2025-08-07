import numpy as np
import matplotlib.pyplot as plt
import itertools

def task_func(n_walks, n_steps, seed=None):
    # Validate inputs
    if not isinstance(n_walks, int) or n_walks <= 0:
        raise ValueError("n_walks must be a positive integer.")
    if not isinstance(n_steps, int) or n_steps <= 0:
        raise ValueError("n_steps must be a positive integer.")
    
    # Set random seed for reproducibility
    if seed is not None:
        np.random.seed(seed)
    
    # Define colors to cycle through
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    color_cycle = itertools.cycle(colors)
    
    # Generate random walks
    walks = np.cumsum(np.random.choice([-1, 1], size=(n_walks, n_steps)), axis=1)
    
    # Plot the walks
    fig, ax = plt.subplots()
    for walk in walks:
        ax.plot(walk, color=next(color_cycle))
    
    # Set plot labels and title
    ax.set_xlabel('Step')
    ax.set_ylabel('Position')
    ax.set_title(f'{n_walks} Random Walks with {n_steps} Steps Each')
    
    # Show the plot
    plt.show()
    
    return ax

# Example usage:
# ax = task_func(5, 100, seed=42)