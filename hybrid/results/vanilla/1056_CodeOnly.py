import numpy as np
import random
import matplotlib.pyplot as plt

# Constants
LETTERS = list("abcdefghijklmnopqrstuvwxyz")
NUMBERS = list(range(1, 27))

def task_func(n_pairs=26):
    # Validate the input
    if not (1 <= n_pairs <= 26):
        raise ValueError("n_pairs must be between 1 and 26, inclusive.")
    
    # Generate all possible letter-number pairs
    pairs = [(letter, number) for letter, number in zip(LETTERS, NUMBERS)]
    
    # Shuffle the pairs
    random.shuffle(pairs)
    
    # Select the first n_pairs from the shuffled list
    selected_pairs = pairs[:n_pairs]
    
    # Assign random counts to each pair
    counts = np.random.randint(1, 10, size=n_pairs)
    
    # Prepare labels for the x-axis
    labels = [f"{letter}:{number}" for letter, number in selected_pairs]
    
    # Create the bar chart
    fig, ax = plt.subplots()
    bars = ax.bar(labels, counts)
    
    # Set the title and labels
    ax.set_title("Random Letter:Number Pairs Chart")
    ax.set_xlabel("Letter:Number Pairs")
    ax.set_ylabel("Counts")
    
    # Display the chart
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
    
    # Return the BarContainer object
    return bars

# Example usage
# task_func(10)