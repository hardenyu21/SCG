import re
from nltk.corpus import words
import nltk

# Ensure the words corpus is downloaded
nltk.download('words')

# Constants
SAMPLE_ENGLISH_WORDS = set(words.words())  # Correct initialization

def task_func(s, n):
    # Convert the string to lowercase to ensure case insensitivity
    s = s.lower()
    
    # Use regex to find all words in the string
    words_in_string = re.findall(r'\b\w+\b', s)
    
    # Filter out only the English words
    english_words = {word for word in words_in_string if word in SAMPLE_ENGLISH_WORDS}
    
    # Return up to n different English words
    return list(english_words)[:n]

# Example usage:
# result = task_func("Hello world! This is a test string with some English words.", 5)
# print(result)