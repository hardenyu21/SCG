import heapq
import random

def task_func(list_length: int = 5, k: int = 3):
    # Generate a random list of integers with the specified length
    random_list = [random.randint(1, 100) for _ in range(list_length)]
    
    # Find the k largest numbers using heapq
    k_largest_numbers = heapq.nlargest(k, random_list)
    
    # Return the tuple containing the random list and the k largest numbers
    return (random_list, k_largest_numbers)

# Example usage:
# result = task_func(10, 3)
# print(result)