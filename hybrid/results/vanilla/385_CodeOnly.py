import matplotlib.pyplot as plt
from collections import Counter

FRUITS = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry', 'Fig', 'Grape', 'Honeydew', 'Indian Prune', 'Jackfruit']

def task_func(fruit_dict):
    # Initialize a Counter to keep track of fruit frequencies
    fruit_counter = Counter()
    
    # Iterate over the dictionary to count each fruit occurrence
    for person, fruit in fruit_dict.items():
        if fruit in FRUITS:
            fruit_counter[fruit] += 1
    
    # Create a bar chart
    fig, ax = plt.subplots()
    ax.bar(fruit_counter.keys(), fruit_counter.values(), color='skyblue')
    ax.set_xlabel('Fruit')
    ax.set_ylabel('Frequency')
    ax.set_title('Fruit Frequency')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Return the dictionary and the axes object
    return dict(fruit_counter), ax

# Example usage:
# fruit_dict = {
#     'Alice': 'Apple',
#     'Bob': 'Banana',
#     'Charlie': 'Apple',
#     'David': 'Cherry',
#     'Eve': 'Banana',
#     'Frank': 'Grape',
#     'Grace': 'Apple'
# }
# fruit_counts, ax = task_func(fruit_dict)
# plt.show()