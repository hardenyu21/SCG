import nltk
nltk.download('stopwords')
from collections import Counter
import os
from nltk.corpus import stopwords

# Constants
STOPWORDS = set(stopwords.words('english'))

def task_func(directory_path):
    unique_words = set()
    
    # Iterate over all files in the specified directory
    for filename in os.listdir(directory_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                # Read the content of the file
                content = file.read()
                # Split the content into words
                words = content.split()
                # Filter out stopwords and add to the set of unique words
                unique_words.update(word.lower() for word in words if word.lower() not in STOPWORDS)
    
    # Return the count of unique non-stop words
    return len(unique_words)

# Example usage:
# print(task_func('/path/to/directory'))