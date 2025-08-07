from functools import reduce
from itertools import permutations
import math

def task_func(numbers):
    # Check if the input is a list of integers
    if not isinstance(numbers, list) or not all(isinstance(n, int) for n in numbers):
        raise TypeError("Input must be a list of integers.")
    
    # Check if all numbers are non-negative
    if any(n < 0 for n in numbers):
        raise ValueError("Input numbers must be non-negative.")
    
    # If the input list is empty, return empty lists
    if not numbers:
        return [], []
    
    # Generate all permutations of the list
    all_perms = list(permutations(numbers))
    
    # Calculate the sum of the factorials for each permutation
    factorial_sums = []
    for perm in all_perms:
        factorial_sum = sum(math.factorial(n) for n in perm)
        factorial_sums.append(factorial_sum)
    
    return factorial_sums, all_perms

# Example usage:
# fac, perm = task_func([0, 4])
# print(fac)  # Output: [25, 25]
# print(perm) # Output: [(0, 4), (4, 0)]