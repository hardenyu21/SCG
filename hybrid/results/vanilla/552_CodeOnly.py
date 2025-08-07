import collections
import itertools
import matplotlib.pyplot as plt

# Constants
ITEMS = ['apple', 'banana']

def task_func(a, b, items=ITEMS):
    # Combine the two lists
    combined_list = list(itertools.chain(a, b))
    
    # Count the frequency of each item in the combined list
    frequency_counter = collections.Counter(combined_list)
    
    # Extract the frequencies of the predefined items
    item_frequencies = [frequency_counter[item] for item in items]
    
    # Create a bar chart
    fig, ax = plt.subplots()
    ax.bar(items, item_frequencies)
    
    # Set labels and title
    ax.set_xlabel('Items')
    ax.set_ylabel('Frequency')
    ax.set_title('Frequency of Predefined Items in Combined List')
    
    # Show the plot
    plt.show()
    
    return ax

# Example usage:
# list1 = ['apple', 'banana', 'apple', 'orange']
# list2 = ['banana', 'apple', 'grape', 'banana']
# task_func(list1, list2)