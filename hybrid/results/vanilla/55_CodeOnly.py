import re
import pandas as pd

STOPWORDS = ["Those", "are", "the", "words", "to", "ignore"]

def task_func(text):
    # Split the text into sentences using regex to handle periods followed by spaces or end of string
    sentences = re.split(r'(?<=[.!?]) +', text.strip())
    
    # Initialize a dictionary to store sentences and their word counts
    sentence_dict = {}
    
    # Iterate over the sentences
    for i, sentence in enumerate(sentences, start=1):
        # Remove punctuation and split the sentence into words
        words = re.findall(r'\b\w+\b', sentence)
        
        # Filter out stopwords and count the remaining words
        word_count = sum(1 for word in words if word not in STOPWORDS)
        
        # Only add non-empty sentences to the dictionary
        if word_count > 0:
            sentence_dict[f"Sentence {i}"] = word_count
    
    # Create a pandas Series from the dictionary
    sentence_series = pd.Series(sentence_dict)
    
    return sentence_series

# Example usage:
# text = "Those are the words to ignore. This is a test sentence. Another sentence here."
# print(task_func(text))