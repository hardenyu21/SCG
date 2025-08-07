import random
import re

def task_func(text, seed=None):
    if seed is not None:
        random.seed(seed)
    
    def scramble_word(word):
        if len(word) <= 3:
            return word
        # Extract the first and last letters
        first, last = word[0], word[-1]
        # Scramble the middle part
        middle = list(word[1:-1])
        random.shuffle(middle)
        # Reconstruct the word
        return first + ''.join(middle) + last
    
    # Use regex to find words and apply scrambling
    scrambled_text = re.sub(r'\b\w+\b', lambda match: scramble_word(match.group()), text)
    
    return scrambled_text