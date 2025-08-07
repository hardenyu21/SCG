from collections import Counter
import itertools
import string

def task_func(word: str) -> dict:
    # Generate all possible two-letter combinations of lowercase English alphabets
    all_combinations = [''.join(p) for p in itertools.product(string.ascii_lowercase, repeat=2)]
    
    # Initialize a dictionary with all combinations and set their counts to 0
    combination_counts = {combo: 0 for combo in all_combinations}
    
    # Create a list of two-letter combinations from the given word
    word_combinations = [word[i:i+2] for i in range(len(word) - 1)]
    
    # Count the frequency of each two-letter combination in the word
    word_counter = Counter(word_combinations)
    
    # Update the dictionary with the counts from the word
    combination_counts.update(word_counter)
    
    return combination_counts