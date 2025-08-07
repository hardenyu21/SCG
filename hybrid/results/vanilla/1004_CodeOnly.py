import urllib.request
import re
from collections import Counter
import matplotlib.pyplot as plt

def task_func(url):
    # Download the text file from the specified URL
    response = urllib.request.urlopen(url)
    text = response.read().decode('utf-8')
    
    # Use a regular expression to find words in the text
    words = re.findall(r'\b\w+\b', text)
    
    # Count the frequency of each word using Counter
    word_counts = Counter(words)
    
    # Get the ten most common words
    most_common_words = word_counts.most_common(10)
    
    # Plot a bar chart of the ten most common words
    words, counts = zip(*most_common_words)
    fig, ax = plt.subplots()
    ax.bar(words, counts)
    ax.set_xlabel('Words')
    ax.set_ylabel('Frequency')
    ax.set_title('Top 10 Most Frequent Words')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Return the Counter object and the Axes object
    return word_counts, ax

# Example usage:
# word_counts, ax = task_func('http://example.com/path/to/textfile.txt')
# plt.show()