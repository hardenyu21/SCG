from nltk.tokenize import RegexpTokenizer
from string import punctuation
import csv
import os

PUNCTUATION = set(punctuation)

def task_func(text, filename):
    # Tokenize the text to find words starting with '$'
    tokenizer = RegexpTokenizer(r'\$\w+')
    words = tokenizer.tokenize(text)
    
    # Filter out words that are solely composed of punctuation characters
    filtered_words = [word for word in words if any(char not in PUNCTUATION for char in word[1:])]
    
    # Define the CSV file path
    csv_file_path = os.path.abspath(filename)
    
    # Write the filtered words to a CSV file
    with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Word']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for word in filtered_words:
            writer.writerow({'Word': word})
    
    # Return the absolute path of the saved CSV file
    return csv_file_path