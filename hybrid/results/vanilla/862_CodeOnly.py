import random
import string
from collections import defaultdict

def task_func(n, seed=None):
    # Set the seed for reproducibility
    random.seed(seed)
    
    # Create a defaultdict with list as the default factory
    letter_dict = defaultdict(list)
    
    # Generate 'n' random letters
    for _ in range(n):
        # Randomly choose a letter from the alphabet
        letter = random.choice(string.ascii_lowercase)
        # Append the letter to its corresponding list in the dictionary
        letter_dict[letter].append(letter)
    
    return letter_dict

# Example usage
print(task_func(30, seed=1))