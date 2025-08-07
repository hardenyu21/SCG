import re
import random
import pandas as pd

def task_func(data_list, seed=None):
    # Set the random seed for reproducibility if provided
    if seed is not None:
        random.seed(seed)
    
    # Initialize lists to store original and shuffled strings
    original_strings = []
    shuffled_strings = []
    
    # Iterate over each string in the input list
    for original_string in data_list:
        # Split the string into substrings based on commas
        substrings = re.split(r'\s*,\s*', original_string.strip())
        
        # Shuffle the substrings
        shuffled_substrings = substrings[:]
        random.shuffle(shuffled_substrings)
        
        # Join the shuffled substrings back into a single string
        shuffled_string = ', '.join(shuffled_substrings)
        
        # Append the original and shuffled strings to their respective lists
        original_strings.append(original_string)
        shuffled_strings.append(shuffled_string)
    
    # Create a DataFrame with the original and shuffled strings
    df = pd.DataFrame({
        'Original String': original_strings,
        'Shuffled String': shuffled_strings
    })
    
    return df

# Example usage:
# data_list = ["apple, banana, cherry", "dog, elephant, frog"]
# df = task_func(data_list, seed=42)
# print(df)