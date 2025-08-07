import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from collections import Counter

# Constants
STOPWORDS = set(stopwords.words('english'))

def task_func(text, n=2):
    # Remove punctuation and convert to lowercase
    text = re.sub(r'[^\w\s]', '', text).lower()
    
    # Split text into words
    words = text.split()
    
    # Remove duplicates and stopwords
    unique_words = []
    seen = set()
    for word in words:
        if word not in STOPWORDS and word not in seen:
            unique_words.append(word)
            seen.add(word)
    
    # Generate n-grams
    ngrams = zip(*[unique_words[i:] for i in range(n)])
    
    # Count n-grams
    ngram_counts = Counter(ngrams)
    
    return dict(ngram_counts)

# Example usage:
# text = "This is a sample text with some sample words and some sample text."
# print(task_func(text))