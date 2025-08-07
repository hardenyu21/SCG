import re
from collections import Counter

def task_func(text, top_n):
    # Remove URLs starting with http or https
    text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)
    
    # Tokenize the text into words
    words = re.findall(r'\b\w+\b', text.lower())
    
    # Count the frequency of each word
    word_counts = Counter(words)
    
    # Get the N most common words
    most_common_words = word_counts.most_common(top_n)
    
    return most_common_words

# Example usage:
# text = "Check out this link: https://example.com. This is a test. This test is only a test."
# top_n = 3
# print(task_func(text, top_n))