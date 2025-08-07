from collections import Counter
import itertools
import random

# Constants
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def task_func(list_of_lists, seed=0):
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # Fill empty lists with a random sample from the alphabet
    filled_lists = [
        sublist if sublist else random.sample(ALPHABET, len(ALPHABET))
        for sublist in list_of_lists
    ]
    
    # Flatten the list of lists into a single list of characters
    all_characters = list(itertools.chain.from_iterable(filled_lists))
    
    # Count the frequency of each letter
    letter_counter = Counter(all_characters)
    
    return letter_counter

# Example usage:
# list_of_lists = [['a', 'b', 'c'], [], ['d', 'e', 'f', 'g']]
# print(task_func(list_of_lists))