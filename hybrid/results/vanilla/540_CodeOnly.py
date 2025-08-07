from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import itertools

def task_func(list_of_menuitems, title="Menu Distribution", color="blue", width=1.0):
    # Flatten the nested list using itertools.chain
    flattened_items = list(itertools.chain.from_iterable(list_of_menuitems))
    
    # Count the occurrences of each item
    item_counts = Counter(flattened_items)
    
    # Sort the items alphabetically
    sorted_items = sorted(item_counts.keys())
    
    # Prepare the data for plotting
    frequencies = [item_counts[item] for item in sorted_items]
    
    # Create the histogram plot
    fig, ax = plt.subplots()
    ax.bar(sorted_items, frequencies, color=color, width=width)
    
    # Set the labels and title
    ax.set_xlabel("Menu Items")
    ax.set_ylabel("Frequency")
    ax.set_title(title)
    
    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45, ha='right')
    
    # Show the plot
    plt.tight_layout()
    plt.show()
    
    return ax

# Example usage:
# list_of_menuitems = [['burger', 'fries'], ['burger', 'soda'], ['fries', 'soda', 'soda']]
# ax = task_func(list_of_menuitems)