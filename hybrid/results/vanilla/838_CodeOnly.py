import re
from nltk.stem import PorterStemmer
import pandas as pd

def task_func(text_series):
    # Initialize the PorterStemmer
    stemmer = PorterStemmer()
    
    # Define a function to process each text
    def process_text(text):
        # Convert to lowercase
        text = text.lower()
        # Remove non-alphanumeric characters except spaces
        text = re.sub(r'[^a-z0-9\s]', '', text)
        # Split the text into words
        words = text.split()
        # Stem each word
        stemmed_words = [stemmer.stem(word) for word in words]
        # Join the stemmed words back into a single string
        return ' '.join(stemmed_words)
    
    # Apply the process_text function to each element in the Series
    processed_series = text_series.apply(process_text)
    
    return processed_series

# Example usage:
# text_series = pd.Series(["Hello, World!", "Pandas are great!"])
# processed_series = task_func(text_series)
# print(processed_series)