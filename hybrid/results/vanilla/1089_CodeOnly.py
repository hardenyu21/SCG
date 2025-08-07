import numpy as np
from collections import Counter

def task_func(list_of_tuples):
    # Initialize sum of numeric values
    sum_of_values = 0
    
    # Initialize a list to hold categories
    categories = []
    
    # Iterate over each tuple in the list
    for numeric_value, category in list_of_tuples:
        # Add the numeric value to the sum
        sum_of_values += numeric_value
        # Append the category to the list
        categories.append(category)
    
    # Count the occurrences of each category
    category_counts = Counter(categories)
    
    # Return the result as a tuple
    return (sum_of_values, dict(category_counts))

# Example usage:
# list_of_tuples = [(10, 'A'), (20, 'B'), (10, 'A'), (30, 'C')]
# result = task_func(list_of_tuples)
# print(result)  # Output: (70, {'A': 2, 'B': 1, 'C': 1})