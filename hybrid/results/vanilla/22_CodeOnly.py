import collections
from itertools import zip_longest
from random import choices

def task_func(l1, l2, K=10):
    # Combine the two lists by alternating their elements
    combined_list = [item for pair in zip_longest(l1, l2) for item in pair if item is not None]
    
    # Create a random sample of size K from the combined list
    sample = choices(combined_list, k=K)
    
    # Calculate the frequency of each element in the sample
    frequency_counter = collections.Counter(sample)
    
    return frequency_counter

# Example usage:
# l1 = [1, 2, 3]
# l2 = ['a', 'b', 'c', 'd', 'e']
# K = 10
# print(task_func(l1, l2, K))