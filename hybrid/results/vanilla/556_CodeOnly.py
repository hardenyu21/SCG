import numpy as np
import random
from difflib import SequenceMatcher

def task_func(s, min_length, max_length, letters):
    # Generate a random length between min_length and max_length
    length = random.randint(min_length, max_length)
    
    # Generate a random string of the determined length
    random_string = ''.join(random.choice(letters) for _ in range(length))
    
    # Calculate the similarity score between the generated string and the provided string s
    similarity_score = SequenceMatcher(None, random_string, s).ratio()
    
    # Determine if the similarity score is above the threshold
    is_similar = similarity_score >= 0.5
    
    # Return the generated string and the similarity boolean
    return (random_string, is_similar)

# Example usage:
# result = task_func("example", 5, 10, "abcdefghijklmnopqrstuvwxyz")
# print(result)