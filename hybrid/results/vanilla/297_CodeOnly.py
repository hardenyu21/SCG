import itertools
import collections

def task_func(elements, subset_size):
    # Generate all possible subsets of the given size
    subsets = itertools.combinations(elements, subset_size)
    
    # Calculate the sum of each subset
    sum_counts = collections.defaultdict(int)
    for subset in subsets:
        subset_sum = sum(subset)
        sum_counts[subset_sum] += 1
    
    # Convert defaultdict to a regular dictionary for output
    return dict(sum_counts)

# Example usage:
elements = (1, 2, 3, 4)
subset_size = 2
result = task_func(elements, subset_size)
print(result)