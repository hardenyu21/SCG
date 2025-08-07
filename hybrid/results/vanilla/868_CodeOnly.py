from itertools import cycle
from random import choice, seed

def task_func(n_colors, colors=['Red', 'Green', 'Blue', 'Yellow', 'Purple'], rng_seed=None):
    if n_colors <= 0:
        return []
    
    if rng_seed is not None:
        seed(rng_seed)
    
    color_cycle = cycle(colors)
    pattern = []
    
    for i in range(n_colors):
        if i % 2 == 0:
            # Use the next color in the cyclic sequence
            pattern.append(next(color_cycle))
        else:
            # Use a random color from the list
            pattern.append(choice(colors))
    
    return pattern

# Example usage:
colors = ['Brown', 'Green', 'Black']
color_pattern = task_func(12, colors=colors, rng_seed=42)
print(color_pattern)