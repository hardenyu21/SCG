import bisect
import random

def task_func(num, list_length=5, min_value=0, max_value=100):
    # Generate a random sorted list of integers
    random_list = sorted(random.randint(min_value, max_value) for _ in range(list_length))
    
    # Insert the number into the sorted list while maintaining order
    bisect.insort(random_list, num)
    
    # Return the original random list and the new sorted list
    return (random_list[:-1], random_list)

# Example usage:
# result = task_func(42)
# print(result)