from collections import Counter
import os
import csv

# Constants
FILE_DIR = './yourdictfiles/'

def task_func(output_file, test_directory):
    try:
        # Check if the directory exists
        if not os.path.isdir(test_directory):
            return 0

        # Initialize a Counter to keep track of word counts
        word_counter = Counter()

        # Iterate over all files in the directory
        for filename in os.listdir(test_directory):
            # Check if the file is a .txt file
            if filename.endswith('.txt'):
                file_path = os.path.join(test_directory, filename)
                # Open and read the file
                with open(file_path, 'r', encoding='utf-8') as file:
                    # Read all lines and split into words
                    words = file.read().split()
                    # Update the counter with words from this file
                    word_counter.update(words)

        # Write the word counts to a CSV file
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            # Write the header
            csv_writer.writerow(['Word', 'Count'])
            # Write the word counts
            for word, count in word_counter.items():
                csv_writer.writerow([word, count])

        # Return the total number of words
        return sum(word_counter.values())

    except Exception as e:
        # Return 0 if any error occurs
        return 0