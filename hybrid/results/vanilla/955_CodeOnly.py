import numpy as np
import matplotlib.pyplot as plt
import re
from collections import Counter

def task_func(mystrings, text):
    # Check if the input text is empty
    if not text.strip():
        raise ValueError("The input text is empty.")
    
    # Convert text to lowercase
    text = text.lower()
    
    # Replace spaces with underscores
    text = text.replace(' ', '_')
    
    # Split the text into words
    words = re.findall(r'\b\w+\b', text)
    
    # Count the frequency of each unique word
    word_counts = Counter(words)
    
    # Extract unique words and their frequencies
    unique_words = list(word_counts.keys())
    frequencies = list(word_counts.values())
    
    # Plot the frequency of each unique word
    fig, ax = plt.subplots()
    ax.bar(unique_words, frequencies)
    ax.set_xlabel('Unique Words')
    ax.set_ylabel('Frequency')
    ax.set_title('Word Frequency Plot')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Return the Axes object
    return ax