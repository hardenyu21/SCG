import re
import string
from nltk.stem import PorterStemmer
from collections import Counter

STEMMER = PorterStemmer()

def task_func(content):
    # Remove punctuation and convert to lowercase
    content = content.translate(str.maketrans('', '', string.punctuation)).lower()
    
    # Split the content into words
    words = content.split()
    
    # Stem all words except the last one
    stemmed_words = [STEMMER.stem(word) for word in words[:-1]]
    
    # Count the frequency of each stemmed word
    frequency = Counter(stemmed_words)
    
    return dict(frequency)

# Example usage:
# print(task_func("The quick brown foxes jumped over the lazy dogs."))