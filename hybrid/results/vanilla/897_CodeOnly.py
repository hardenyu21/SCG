import numpy as np
import matplotlib.pyplot as plt
import random

# Constants
NUMBERS = list(range(1, 7))  # Adjusting for dice rolls (1 to 6)

def task_func(rolls, seed=None):
    # Set the random seed for reproducibility if provided
    if seed is not None:
        random.seed(seed)
    
    # Simulate dice rolls
    dice_rolls = [random.randint(1, 6) for _ in range(rolls)]
    
    # Calculate the frequency of each outcome
    frequency = np.array([dice_rolls.count(i) for i in NUMBERS])
    
    # Plot the histogram
    fig, ax = plt.subplots()
    ax.hist(dice_rolls, bins=range(1, 8), align='left', rwidth=0.8, color='blue', edgecolor='black')
    ax.set_title("Histogram of Dice Rolls")
    ax.set_xlabel("Dice Value")
    ax.set_ylabel("Frequency")
    ax.set_xticks(NUMBERS)
    
    # Return the frequency array and the Axes object
    return frequency, ax

# Example usage:
# frequency, ax = task_func(1000, seed=42)
# plt.show()