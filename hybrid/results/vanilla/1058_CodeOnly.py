import itertools
import seaborn as sns
import matplotlib.pyplot as plt

# Constants
SHAPES = [
    "Circle",
    "Square",
    "Triangle",
    "Rectangle",
    "Pentagon",
    "Hexagon",
    "Heptagon",
    "Octagon",
    "Nonagon",
    "Decagon",
]
COLORS = [
    "Red",
    "Blue",
    "Green",
    "Yellow",
    "Black",
    "White",
    "Purple",
    "Orange",
    "Pink",
    "Brown",
]

def task_func(num_pairs=10):
    # Generate all possible shape-color combinations
    all_combinations = list(itertools.product(SHAPES, COLORS))
    
    # Select the specified number of unique combinations
    selected_combinations = all_combinations[:num_pairs]
    
    # Flatten the list of tuples into a single list of strings
    combination_labels = [f"{shape}-{color}" for shape, color in selected_combinations]
    
    # Create a countplot
    plt.figure(figsize=(10, 6))
    ax = sns.countplot(y=combination_labels, order=combination_labels)
    
    # Set plot title and labels
    ax.set_title(f"Countplot of {num_pairs} Shape-Color Combinations")
    ax.set_xlabel("Count")
    ax.set_ylabel("Shape-Color Pair")
    
    # Show the plot
    plt.tight_layout()
    plt.show()
    
    return ax

# Example usage
ax = task_func(10)