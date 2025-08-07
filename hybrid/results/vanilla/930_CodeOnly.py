import random
import string

POSSIBLE_LETTERS = ['a', 'b', 'c']

def task_func(word):
    # Check if the input contains only letters
    if not word.isalpha():
        raise ValueError("Input contains non-letter characters.")
    
    # If the word has fewer than 2 letters, return a list of empty strings
    if len(word) < 2:
        return ['' for _ in POSSIBLE_LETTERS]
    
    # Generate a list of adjacent letter pairs
    adjacent_pairs = [word[i:i+2] for i in range(len(word) - 1)]
    
    # Randomly select pairs equal to the length of POSSIBLE_LETTERS
    selected_pairs = random.sample(adjacent_pairs, min(len(adjacent_pairs), len(POSSIBLE_LETTERS)))
    
    # If there are fewer pairs than POSSIBLE_LETTERS, fill with empty strings
    result = selected_pairs + ['' for _ in range(len(POSSIBLE_LETTERS) - len(selected_pairs))]
    
    return result