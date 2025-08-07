from collections import defaultdict
import re

def task_func(word: str) -> dict:
    # Sanitize the word to include only alphabetic characters
    sanitized_word = re.sub(r'[^a-zA-Z]', '', word)
    
    # Initialize a defaultdict to store two-letter combinations and their counts
    two_letter_counts = defaultdict(int)
    
    # Iterate over the sanitized word to find two-letter combinations
    for i in range(len(sanitized_word) - 1):
        # Extract the two-letter combination
        two_letter_combination = sanitized_word[i:i+2]
        # Increment the count for this combination
        two_letter_counts[two_letter_combination] += 1
    
    return two_letter_counts