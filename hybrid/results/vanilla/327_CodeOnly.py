import csv
import re
from collections import Counter

def task_func(file_path, regex_pattern=r'\(.+?\)|\w+|[\W_]+'):
    # Initialize a list to store all matches
    all_matches = []

    # Open the CSV file
    with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        # Create a CSV reader object
        csvreader = csv.reader(csvfile)

        # Iterate over each row in the CSV file
        for row in csvreader:
            # Iterate over each cell in the row
            for cell in row:
                # Find all matches in the cell using the regex pattern
                matches = re.findall(regex_pattern, cell)
                # Extend the list of all matches
                all_matches.extend(matches)

    # Count the occurrences of each match
    match_counts = Counter(all_matches)

    # Convert the Counter object to a dictionary and return it
    return dict(match_counts)

# Example usage:
# result = task_func('example.csv')
# print(result)