import json
from collections import Counter
import random

def task_func(my_dict, keys):
    # Check if 'keys' contains exactly 10 unique elements
    if len(set(keys)) != 10:
        raise ValueError("The 'keys' parameter must contain exactly 10 unique elements.")
    
    # Add 10 random elements to the dictionary
    for key in keys:
        my_dict[key] = random.randint(1, 100)
    
    # Save the JSON representation of the updated dictionary to a file
    json_filename = 'updated_dictionary.json'
    with open(json_filename, 'w') as json_file:
        json.dump(my_dict, json_file, indent=4)
    
    # Count the occurrences of each key
    key_counts = Counter(my_dict.keys())
    
    # Save the counts of each key to a separate text file
    txt_filename = 'key_frequencies.txt'
    with open(txt_filename, 'w') as txt_file:
        for key, count in key_counts.items():
            txt_file.write(f"{key}: {count}\n")
    
    # Return the dictionary and the paths to the files
    return my_dict, json_filename, txt_filename