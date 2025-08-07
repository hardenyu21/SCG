import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

def task_func(text_dict, word_keys, top_k=2):
    # Validate top_k
    if top_k < 0:
        raise ValueError("top_k must be a non-negative integer.")
    
    # Calculate frequencies for the provided word_keys
    word_frequencies = {word: text_dict.get(word, 0) for word in word_keys}
    
    # Get the top_k most common words and their frequencies
    counter = Counter(text_dict)
    top_k_common_words = counter.most_common(top_k)
    top_k_frequencies = {word: freq for word, freq in top_k_common_words}
    
    # Create a bar chart
    fig, ax = plt.subplots()
    ax.bar(word_frequencies.keys(), word_frequencies.values(), color='skyblue')
    ax.set_xlabel('Words')
    ax.set_ylabel('Frequencies')
    ax.set_title('Word Frequencies')
    plt.xticks(rotation=45)
    
    # Return the Axes object and the dictionary of top_k frequencies
    return ax, top_k_frequencies

# Example usage:
# text_dict = {'apple': 4, 'banana': 2, 'orange': 5, 'grape': 3}
# word_keys = ['apple', 'banana', 'kiwi']
# ax, top_k_frequencies = task_func(text_dict, word_keys, top_k=3)
# plt.show()
# print(top_k_frequencies)