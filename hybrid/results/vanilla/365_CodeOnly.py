from collections import Counter
import json
import random

# Constants
WORDS = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew']

def task_func(n, file_name, seed=77):
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # Randomly select n words from the WORDS list
    selected_words = random.sample(WORDS, min(n, len(WORDS)))
    
    # Count the occurrences of each word
    word_count = Counter(selected_words)
    
    # Write the word count to a JSON file
    with open(file_name, 'w') as json_file:
        json.dump(word_count, json_file, indent=4)
    
    # Return the name of the generated JSON file
    return file_name

# Example usage:
# file_name = task_func(5, 'word_count.json')
# print(f"JSON file generated: {file_name}")