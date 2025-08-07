import re
from collections import Counter
import matplotlib.pyplot as plt

def task_func(text):
    # Lowercase the text
    text = text.lower()
    
    # Remove punctuation using regex
    text = re.sub(r'[^\w\s]', '', text)
    
    # Split the text into words
    words = text.split()
    
    # Count the frequency of each word
    word_counts = Counter(words)
    
    # Get the 10 most common words
    most_common_words = word_counts.most_common(10)
    
    # Plot the top 10 most common words
    words, counts = zip(*most_common_words)
    fig, ax = plt.subplots()
    ax.bar(words, counts)
    ax.set_xlabel('Words')
    ax.set_ylabel('Counts')
    ax.set_title('Top 10 Most Common Words')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Return the list of tuples and the Axes object
    return most_common_words, ax

# Example usage:
# text = "Your sample text goes here."
# most_common_words, ax = task_func(text)
# plt.show()