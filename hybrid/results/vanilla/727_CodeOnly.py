import re
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

# Constants
SENTENCES = ['This is a sentence', 'Another sentence here', 'More sentences']

def task_func(s: str) -> np.ndarray:
    # Combine the input string with the predefined sentences
    all_sentences = SENTENCES + [s]
    
    # Initialize the CountVectorizer
    vectorizer = CountVectorizer()
    
    # Fit and transform the sentences to create the bag-of-words model
    X = vectorizer.fit_transform(all_sentences)
    
    # Get the vector for the input string
    # The input string is the last one in the list, so we take the last row
    input_vector = X.toarray()[-1]
    
    return input_vector

# Example usage:
# vector = task_func("This is a test sentence")
# print(vector)