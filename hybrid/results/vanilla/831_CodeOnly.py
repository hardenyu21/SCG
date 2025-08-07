import random
import math

def task_func(range_start=1, range_end=100, pairs_count=10, random_seed=None):
    if random_seed is not None:
        random.seed(random_seed)
    
    for _ in range(pairs_count):
        num1 = random.randint(range_start, range_end)
        num2 = random.randint(range_start, range_end)
        abs_diff = abs(num1 - num2)
        sqrt_diff = math.sqrt(abs_diff)
        yield (num1, num2, sqrt_diff)

# Example usage:
pairs = task_func(1, 3, pairs_count=25, random_seed=14)
print(next(pairs))  # Output: (1, 3, 1.4142135623730951)