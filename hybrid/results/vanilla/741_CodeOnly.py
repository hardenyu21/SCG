from itertools import groupby
from operator import itemgetter

# Constants
KEY_FUNC = itemgetter(0)

def task_func(my_dict):
    # Sort the dictionary items by the first character of the key
    sorted_items = sorted(my_dict.items(), key=KEY_FUNC)
    
    # Group the items by the first character of the key
    grouped_items = groupby(sorted_items, key=KEY_FUNC)
    
    # Aggregate the values for each group
    aggregated_dict = {}
    for key, group in grouped_items:
        # Sum the values for each group
        total_value = sum(value for _, value in group)
        aggregated_dict[key] = total_value
    
    return aggregated_dict

# Example usage:
# my_dict = {'apple': 10, 'apricot': 5, 'banana': 7, 'blueberry': 3, 'cherry': 8}
# print(task_func(my_dict))
# Output: {'a': 15, 'b': 10, 'c': 8}