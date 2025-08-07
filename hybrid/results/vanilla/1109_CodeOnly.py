import os
from nltk import word_tokenize

def task_func(file_path='File.txt'):
    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    # Initialize an empty list to store tokens
    tokens = []
    
    # Open the file and read line by line
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Tokenize each line and extend the tokens list
            tokens.extend(word_tokenize(line))
    
    return tokens