import string
import re

def task_func(text: str) -> tuple:
    # Count words
    words = text.split()
    num_words = len(words)
    
    # Count characters (excluding whitespace and punctuation)
    # Remove punctuation using regex
    cleaned_text = re.sub(f"[{re.escape(string.punctuation)}]", "", text)
    # Remove whitespace
    cleaned_text = cleaned_text.replace(" ", "")
    num_characters = len(cleaned_text)
    
    # Count unique characters
    unique_characters = set(cleaned_text)
    num_unique_characters = len(unique_characters)
    
    return (num_words, num_characters, num_unique_characters)

# Example usage:
# result = task_func("Hello, world! This is a test.")
# print(result)  # Output: (6, 21, 10)