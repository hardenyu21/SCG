from collections import Counter
import random

def task_func(length, count, seed=0):
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # Define the fixed set of letters
    letters = ['a', 'b', 'c', 'd', 'e']
    
    # Generate the specified number of random strings
    random_strings = [''.join(random.choices(letters, k=length)) for _ in range(count)]
    
    # Concatenate all strings into a single string to count letter frequencies
    all_letters = ''.join(random_strings)
    
    # Use Counter to count the frequency of each letter
    letter_frequency = Counter(all_letters)
    
    return letter_frequency

# Example usage:
# length = 5, count = 10, seed = 42
# This will generate 10 random strings of length 5 using the letters 'a', 'b', 'c', 'd', 'e'
# and return the frequency of each letter in the generated strings.
result = task_func(5, 10, 42)
print(result)