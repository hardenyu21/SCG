import re
import string

# Constants
PUNCTUATION = string.punctuation

def task_func(text):
    # Use regex to find all words
    words = re.findall(r'\b\w+\b', text)
    num_words = len(words)
    
    # Use regex to find all punctuation marks
    punctuation_marks = re.findall(f'[{re.escape(PUNCTUATION)}]', text)
    num_punctuation_marks = len(punctuation_marks)
    
    return (num_words, num_punctuation_marks)

# Example usage:
# text = "Hello, world! How's it going?"
# print(task_func(text))  # Output: (5, 3)