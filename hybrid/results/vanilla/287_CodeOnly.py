from collections import Counter
import os
import json

def task_func(filename, directory):
    word_counts = Counter()
    
    # Iterate over all files in the specified directory
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    # Read the file and count words
                    words = f.read().split()
                    word_counts.update(words)
    
    # Export the word counts to a JSON file
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(word_counts, json_file, ensure_ascii=False, indent=4)
    
    # Return the total number of words
    return sum(word_counts.values())

# Example usage:
# total_words = task_func('word_counts.json', '/path/to/directory')
# print(f"Total number of words: {total_words}")