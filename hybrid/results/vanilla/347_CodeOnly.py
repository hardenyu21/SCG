import pandas as pd
import re
import numpy as np

# Constants
PATTERN = r"([a-fA-F\d]{32})"

def task_func(df, column):
    # Check if the column exists in the DataFrame
    if column not in df.columns:
        raise KeyError(f"The column '{column}' does not exist in the DataFrame.")
    
    # Initialize a list to store all matches
    all_matches = []
    
    # Compile the regex pattern for efficiency
    regex = re.compile(PATTERN)
    
    # Iterate over each entry in the specified column
    for entry in df[column]:
        # Find all matches in the current entry
        matches = regex.findall(str(entry))
        # Extend the list of all matches
        all_matches.extend(matches)
    
    # Count the occurrences of each unique match
    match_counts = pd.Series(all_matches).value_counts()
    
    return match_counts

# Example usage:
# df = pd.DataFrame({'data': ['1234567890abcdef1234567890abcdef', 'abcdef1234567890abcdef1234567890', '1234567890abcdef1234567890abcdef']})
# print(task_func(df, 'data'))