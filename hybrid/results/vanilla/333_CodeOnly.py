import heapq
import random

def task_func(k, list_length=5, min_value=0, max_value=100):
    # Generate a random list of integers
    random_list = [random.randint(min_value, max_value) for _ in range(list_length)]
    
    # Find the k smallest numbers using heapq
    k_smallest = heapq.nsmallest(k, random_list)
    
    # Return the tuple containing the random list and the k smallest numbers
    return (random_list, k_smallest)

# Example usage:
# result = task_func(3, 10, 0, 50)
# print(result)