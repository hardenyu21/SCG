import random
import string
from collections import Counter

def task_func(num_strings, string_length):
    # Generate a list of random strings
    random_strings = [''.join(random.choices(string.ascii_lowercase, k=string_length)) for _ in range(num_strings)]
    
    # Concatenate all strings into a single string
    all_characters = ''.join(random_strings)
    
    # Count the frequency of each character
    character_counts = Counter(all_characters)
    
    # Sort characters by frequency in descending order
    sorted_characters = sorted(character_counts.items(), key=lambda item: item[1], reverse=True)
    
    return sorted_characters

# Example usage:
# result = task_func(10, 5)
# print(result)