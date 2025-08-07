import math
import itertools
from functools import reduce

def task_func(numbers):
    total_log_sum = 0.0
    
    # Iterate over all possible lengths of combinations
    for r in range(1, len(numbers) + 1):
        # Generate all combinations of the current length
        for combination in itertools.combinations(numbers, r):
            # Compute the product of the numbers in the combination
            product = reduce(lambda x, y: x * y, combination)
            # Compute the logarithm of the product
            log_product = math.log(product)
            # Add the logarithm to the total sum
            total_log_sum += log_product
    
    return total_log_sum

# Example usage:
# numbers = [1, 2, 3]
# result = task_func(numbers)
# print(result)