from nltk.tokenize import RegexpTokenizer
from string import punctuation
import os

def task_func(text, output_filename):
    # Tokenizer to extract words starting with '$'
    tokenizer = RegexpTokenizer(r'\$\w+')
    # Extract words starting with '$'
    words = tokenizer.tokenize(text)
    
    # Filter out words that are solely composed of punctuation characters
    filtered_words = [word for word in words if any(char not in punctuation for char in word[1:])]
    
    # Get the absolute path of the output file
    output_path = os.path.abspath(output_filename)
    
    # Write the filtered words to the output file
    with open(output_path, 'w') as file:
        for word in filtered_words:
            file.write(word + '\n')
    
    # Return the absolute path to the output file
    return output_path