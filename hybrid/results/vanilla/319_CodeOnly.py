import re
import matplotlib.pyplot as plt
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk

# Ensure you have the necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

def task_func(example_str, top_n=30):
    # Remove text enclosed in square brackets
    cleaned_str = re.sub(r'\[.*?\]', '', example_str)
    
    # Tokenize the text into words
    words = word_tokenize(cleaned_str)
    
    # Convert to lowercase and filter out stopwords and non-alphabetic tokens
    stop_words = set(stopwords.words('english'))
    filtered_words = [word.lower() for word in words if word.isalpha() and word.lower() not in stop_words]
    
    # Create a frequency distribution
    freq_dist = FreqDist(filtered_words)
    
    # Plot the frequency distribution
    fig, ax = plt.subplots(figsize=(10, 6))
    freq_dist.plot(top_n, cumulative=False, ax=ax)
    plt.title('Word Frequency Distribution')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.show()
    
    # Get the top_n most common words
    top_words = freq_dist.most_common(top_n)
    top_words_dict = {word: freq for word, freq in top_words}
    
    return ax, top_words_dict

# Example usage:
# ax, top_words = task_func("This is a sample text [with some text in brackets] and some more text.")
# print(top_words)