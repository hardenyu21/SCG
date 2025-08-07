import numpy as np
import random

def task_func(MIN_WORDS, MAX_WORDS, WORDS_POOL):
    # Ensure the pool has at least one word
    if not WORDS_POOL:
        raise ValueError("WORDS_POOL must contain at least one word.")
    
    # Randomly choose the number of words in the palindrome
    num_words = random.randint(MIN_WORDS, MAX_WORDS)
    
    # If the number of words is odd, we need a middle word
    if num_words % 2 == 1:
        middle_word = random.choice(WORDS_POOL)
        num_words -= 1  # Adjust for the middle word
    
    # Randomly select half of the words for the first half of the sentence
    half_words = random.sample(WORDS_POOL, num_words // 2)
    
    # Create the palindrome by mirroring the first half
    if num_words % 2 == 1:
        # If odd, include the middle word
        palindrome_words = half_words + [middle_word] + half_words[::-1]
    else:
        # If even, just mirror the first half
        palindrome_words = half_words + half_words[::-1]
    
    # Join the words into a sentence
    palindrome_sentence = ' '.join(palindrome_words)
    
    return palindrome_sentence

# Example usage:
# WORDS_POOL = ["apple", "banana", "cherry", "date", "elderberry"]
# MIN_WORDS = 3
# MAX_WORDS = 7
# sentence = task_func(MIN_WORDS, MAX_WORDS, WORDS_POOL)
# print(sentence)
# print(MIN_WORDS <= len(sentence.split()) <= MAX_WORDS)