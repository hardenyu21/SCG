import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import re

def task_func(example_str):
    # Extract text not enclosed in square brackets
    extracted_text = re.sub(r'\[.*?\]', '', example_str)
    
    # Split the text into words
    words = extracted_text.split()
    
    # Create a TF-IDF vectorizer
    vectorizer = TfidfVectorizer()
    
    # Fit and transform the words into a TF-IDF matrix
    tfidf_matrix = vectorizer.fit_transform([' '.join(words)])
    
    # Get feature names (words)
    feature_names = vectorizer.get_feature_names_out()
    
    # Get the TF-IDF scores
    tfidf_scores = tfidf_matrix.toarray()[0]
    
    # Create a dictionary with words as keys and TF-IDF scores as values
    tfidf_dict = {word: score for word, score in zip(feature_names, tfidf_scores)}
    
    return tfidf_dict

# Example usage:
example_str = "This is a sample text [with some text in brackets] and more text."
print(task_func(example_str))