import pandas as pd
import re
import random

def task_func(data_list, seed=None):
    # Set the random seed for reproducibility if provided
    if seed is not None:
        random.seed(seed)
    
    # Initialize lists to store original and modified strings
    original_strings = []
    modified_strings = []
    
    # Iterate over each string in the input list
    for original_string in data_list:
        # Split the string into a list of substrings using comma as the delimiter
        substrings = original_string.split(',')
        
        # Check if there are any substrings to remove
        if substrings:
            # Randomly select a substring to remove
            substring_to_remove = random.choice(substrings)
            
            # Remove the selected substring from the list
            substrings.remove(substring_to_remove)
            
            # Join the remaining substrings back into a modified string
            modified_string = ','.join(substrings)
        else:
            # If there are no substrings, the modified string is the same as the original
            modified_string = original_string
        
        # Append the original and modified strings to their respective lists
        original_strings.append(original_string)
        modified_strings.append(modified_string)
    
    # Create a pandas DataFrame with the original and modified strings
    df = pd.DataFrame({
        'Original String': original_strings,
        'Modified String': modified_strings
    })
    
    return df

# Example usage:
# data_list = ["apple,banana,cherry", "dog,cat", "red,green,blue,yellow"]
# df = task_func(data_list, seed=42)
# print(df)