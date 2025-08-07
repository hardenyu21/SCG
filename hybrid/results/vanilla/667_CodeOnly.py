import heapq
import collections

def task_func(x, n):
    # Use a heap to find the n most common letters
    # The heap will store tuples of (-frequency, letter) to get the max heap behavior
    heap = [(-freq, letter) for letter, freq in x.items()]
    heapq.heapify(heap)
    
    # Extract the n most common letters
    most_common = heapq.nsmallest(n, heap)
    
    # Return only the letters, sorted by their original frequency in descending order
    return [letter for _, letter in sorted(most_common, key=lambda x: (-x[0], x[1]))]

# Example usage:
# x = {'a': 5, 'b': 2, 'c': 8, 'd': 3}
# n = 2
# print(task_func(x, n))  # Output: ['c', 'a']