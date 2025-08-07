import string
import random
from collections import Counter

def task_func(n, seed=None):
    # Set the seed for consistent randomness if provided
    if seed is not None:
        random.seed(seed)
    
    # Generate a list of random lowercase letters
    letters = [random.choice(string.ascii_lowercase) for _ in range(n)]
    
    # Count the occurrences of each letter using Counter
    letter_counts = Counter(letters)
    
    return letter_counts

# Example usage:
# result = task_func(100, seed=42)
# print(result)