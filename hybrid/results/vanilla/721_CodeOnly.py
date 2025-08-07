import os
import csv
from collections import Counter

def task_func(file_path):
    # Check if the file exists
    if not os.path.exists(file_path):
        return None
    
    # Initialize a Counter to keep track of word frequencies
    word_counter = Counter()
    
    try:
        # Open the CSV file
        with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
            # Create a CSV reader
            csvreader = csv.reader(csvfile)
            
            # Iterate over each row in the CSV file
            for row in csvreader:
                # Iterate over each cell in the row
                for cell in row:
                    # Split the cell content into words and update the counter
                    words = cell.split()
                    word_counter.update(words)
    
    except Exception as e:
        # Return None if an error occurs (e.g., file is empty or unreadable)
        return None
    
    # Find the most common word and its frequency
    if word_counter:
        most_common_word, frequency = word_counter.most_common(1)[0]
        return (most_common_word, frequency)
    else:
        return None