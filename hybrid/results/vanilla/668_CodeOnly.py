import itertools
import math

def task_func(x):
    # Extract the keys and their corresponding lengths
    keys = list(x.keys())
    lengths = list(x.values())
    
    # Initialize variables to track the minimum length and the corresponding subsequence
    min_length = math.inf
    min_subsequence = []
    
    # Iterate over all possible subsequences of the keys
    for r in range(1, len(keys) + 1):
        for subseq in itertools.combinations(keys, r):
            # Calculate the total length of the current subsequence
            total_length = sum(x[key] for key in subseq)
            
            # Update the minimum length and subsequence if a shorter one is found
            if total_length < min_length:
                min_length = total_length
                min_subsequence = list(subseq)
    
    return min_subsequence

# Example usage:
# x = {'a': 3, 'b': 1, 'c': 2}
# print(task_func(x))  # Output: ['b']