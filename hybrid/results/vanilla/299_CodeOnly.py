import itertools
import math
from pandas import Series

def task_func(elements, subset_size, top_n=2):
    # If the subset size is larger than the tuple length or is 0, return 1 and an empty Series
    if subset_size > len(elements) or subset_size == 0:
        return 1, Series([])

    # Generate all subsets of the given size
    subsets = list(itertools.combinations(elements, subset_size))
    
    # Calculate the sum of each subset
    subset_sums = [sum(subset) for subset in subsets]
    
    # Calculate the product of the sums of the subsets
    product_of_sums = math.prod(subset_sums)
    
    # Get the top_n sums of the subsets
    top_sums = sorted(subset_sums, reverse=True)[:top_n]
    
    # Return the product of the sums and the top_n sums as a pandas Series
    return product_of_sums, Series(top_sums)

# Example usage:
# elements = (1, 2, 3, 4)
# subset_size = 2
# top_n = 3
# result = task_func(elements, subset_size, top_n)
# print(result)