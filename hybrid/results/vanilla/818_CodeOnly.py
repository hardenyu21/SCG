import re
import string

# Constants
PUNCTUATION = string.punctuation

def task_func(text):
    # Remove punctuation using regex
    text_no_punctuation = re.sub(f"[{re.escape(PUNCTUATION)}]", "", text)
    # Convert text to lowercase
    text_lower = text_no_punctuation.lower()
    # Split text into words
    cleaned_words = text_lower.split()
    return cleaned_words

# Example usage:
# text = "Hello, World! This is a test."
# print(task_func(text))
# Output: ['hello', 'world', 'this', 'is', 'a', 'test']