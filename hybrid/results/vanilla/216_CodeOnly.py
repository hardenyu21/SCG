import os
import json
from collections import Counter
import re

def task_func(json_dir_path, word_count):
    # Initialize a list to store all words from the JSON files
    all_words = []

    # Iterate over all files in the specified directory
    for filename in os.listdir(json_dir_path):
        if filename.endswith('.json'):
            file_path = os.path.join(json_dir_path, filename)
            try:
                # Open and load the JSON file
                with open(file_path, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    
                    # Extract text content from the JSON data
                    # This assumes that the text is stored in a field named 'text'
                    # You may need to adjust this based on the actual structure of your JSON files
                    if 'text' in data:
                        text = data['text']
                        # Use regex to find words and convert them to lowercase
                        words = re.findall(r'\b\w+\b', text.lower())
                        all_words.extend(words)
            except (json.JSONDecodeError, FileNotFoundError, PermissionError) as e:
                print(f"Error processing {file_path}: {e}")

    # Count the frequency of each word
    word_counts = Counter(all_words)

    # Get the most common words and their counts
    most_common_words = word_counts.most_common(word_count)

    return most_common_words

# Example usage:
# result = task_func('/path/to/json/files', 10)
# print(result)