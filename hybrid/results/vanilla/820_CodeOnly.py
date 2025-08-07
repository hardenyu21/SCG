import random
import string

# Constants
LETTERS = string.ascii_letters

def task_func(num_words, word_length):
    if num_words < 0 or word_length < 0:
        raise ValueError("num_words and word_length must be non-negative.")
    
    words = []
    for _ in range(num_words):
        word = ''.join(random.choice(LETTERS) for _ in range(word_length))
        words.append(word)
    
    return words

# Example usage:
# print(task_func(5, 8))