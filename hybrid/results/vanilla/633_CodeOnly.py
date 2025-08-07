import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

# Ensure the stopwords are downloaded
import nltk
nltk.download('stopwords')
nltk.download('punkt')

def task_func(text: str) -> dict:
    # Define a set of common English stopwords
    stop_words = set(stopwords.words('english'))
    
    # Tokenize the text into words
    words = word_tokenize(text.lower())
    
    # Remove punctuation and stopwords, and filter out duplicate words
    filtered_words = []
    seen = set()
    for word in words:
        if word.isalpha() and word not in stop_words and word not in seen:
            filtered_words.append(word)
            seen.add(word)
    
    # Create a frequency distribution of the remaining words
    frequency_distribution = Counter(filtered_words)
    
    return dict(frequency_distribution)

# Example usage
print(task_func("hello hello world"))  # Output: {'hello': 1, 'world': 1}