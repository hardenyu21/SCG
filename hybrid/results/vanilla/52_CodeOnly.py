import pandas as pd
import regex as re

# Constants
STOPWORDS = ["a", "an", "the", "in", "is", "are"]

def task_func(text):
    # Convert text to lowercase
    text = text.lower()
    
    # Remove punctuation using regex
    text = re.sub(r'[^\w\s]', '', text)
    
    # Split text into words
    words = text.split()
    
    # Filter out stopwords
    filtered_words = [word for word in words if word not in STOPWORDS]
    
    # Count the frequency of each word
    word_counts = pd.Series(filtered_words).value_counts()
    
    return word_counts

# Example usage:
# text = "The quick brown fox jumps over the lazy dog. The dog was not amused."
# print(task_func(text))