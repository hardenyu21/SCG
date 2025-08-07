from collections import Counter
import random

LETTERS = ['a', 'b', 'c', 'd', 'e']

def task_func(count, seed=0):
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # Generate random letter pairs
    letter_pairs = []
    for _ in range(count):
        pair = random.choice(LETTERS) + random.choice(LETTERS)
        letter_pairs.append(pair)
    
    # Count the frequency of each letter pair
    pair_counter = Counter(letter_pairs)
    
    return pair_counter

# Example usage:
# result = task_func(100)
# print(result)