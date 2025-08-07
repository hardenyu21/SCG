import re
from collections import Counter

def task_func(sentence):
    # Use regular expression to find all words in the sentence
    words = re.findall(r'\b\w+\b', sentence.lower())
    # Use Counter to count occurrences of each word
    word_count = Counter(words)
    # Convert Counter object to dictionary and return
    return dict(word_count)

# Example usage:
# sentence = "This is a test. This test is only a test."
# print(task_func(sentence))
# Output: {'this': 2, 'is': 2, 'a': 2, 'test': 3, 'only': 1}