import nltk
from string import punctuation
import pandas as pd

def task_func(text):
    # Check if the input is a string
    if not isinstance(text, str):
        raise ValueError("Input text must be a string.")
    
    # Tokenize the text into words
    words = text.split()
    
    # Filter words that start with '$' and are not entirely punctuation
    filtered_words = [word for word in words if word.startswith('$') and not all(char in punctuation for char in word[1:])]
    
    # Count the occurrences of each word
    word_counts = nltk.FreqDist(filtered_words)
    
    # Create a DataFrame from the word counts
    df = pd.DataFrame(word_counts.items(), columns=['Word', 'Frequency'])
    
    return df

# Example usage
text = "$hello this i$s a $test $test $test"
print(task_func(text))