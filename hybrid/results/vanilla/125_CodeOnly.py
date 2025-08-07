from collections import defaultdict
import itertools
import json
import random

def task_func(LETTERS, n):
    # Generate all possible combinations of the given letters of length 'n'
    combinations = itertools.product(LETTERS, repeat=n)
    
    # Initialize a dictionary to count occurrences of each letter
    letter_counts = defaultdict(int)
    
    # Count occurrences of each letter in all combinations
    for combination in combinations:
        for letter in combination:
            letter_counts[letter] += 1
    
    # Generate a random number between 0 and 100 for the file name
    random_number = random.randint(0, 100)
    file_name = f"prefix_{random_number}.json"
    
    # Save the letter counts to a JSON file
    with open(file_name, 'w') as json_file:
        json.dump(letter_counts, json_file, indent=4)
    
    # Return the name of the generated JSON file
    return file_name