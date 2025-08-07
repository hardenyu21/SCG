import pandas as pd
import random
import re

def task_func(data_list, seed=42):
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # Function to normalize spaces and randomize the order of substrings
    def randomize_and_normalize(s):
        # Normalize spaces: ensure a single space follows each comma
        normalized = re.sub(r'\s*,\s*', ', ', s)
        # Split the string into substrings
        substrings = normalized.split(', ')
        # Randomize the order of substrings
        random.shuffle(substrings)
        # Join the substrings back into a single string
        randomized = ', '.join(substrings)
        return randomized
    
    # Apply the function to each string in the list
    randomized_list = [randomize_and_normalize(s) for s in data_list]
    
    # Create a DataFrame with original and randomized strings
    df = pd.DataFrame({
        'Original String': data_list,
        'Randomized String': randomized_list
    })
    
    return df

# Example usage:
data_list = [
    "apple, banana, cherry",
    "dog, cat, mouse",
    "red, blue, green, yellow"
]

df = task_func(data_list)
print(df)