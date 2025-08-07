import nltk
from string import punctuation
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter

# Constants
PUNCTUATION = set(punctuation)

def task_func(text):
    # Tokenize the text into words
    words = nltk.word_tokenize(text)
    
    # Filter words that start with '$' and contain more than just punctuation
    filtered_words = [word for word in words if word.startswith('$') and any(char not in PUNCTUATION for char in word[1:])]
    
    # Count the frequency of each filtered word
    word_counts = Counter(filtered_words)
    
    # If there are no valid words, return None
    if not word_counts:
        return None
    
    # Create a bar plot
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(x=list(word_counts.keys()), y=list(word_counts.values()))
    ax.set_title('Frequency of Words Starting with "$"')
    ax.set_xlabel('Words')
    ax.set_ylabel('Frequency')
    
    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)
    
    # Show the plot
    plt.tight_layout()
    plt.show()
    
    return ax

# Example usage:
# text = "The $price of $AAPL is $150. $!$ is not counted, but $USD is."
# task_func(text)