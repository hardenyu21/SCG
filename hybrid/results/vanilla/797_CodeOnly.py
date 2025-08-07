import re
import pandas as pd

def task_func(df: pd.DataFrame) -> int:
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame")
    
    # Define the pattern to match brackets
    pattern = r'[(){}[\]]'
    
    # Initialize a counter for brackets
    total_brackets = 0
    
    # Iterate over each element in the DataFrame
    for column in df.columns:
        for value in df[column]:
            # Convert the value to string and find all matches of the pattern
            if isinstance(value, str):
                matches = re.findall(pattern, value)
                # Increment the counter by the number of matches
                total_brackets += len(matches)
    
    return total_brackets

# Example usage
df = pd.DataFrame({'Test': ['(a)', 'b', '[[[[))c']})
print(task_func(df))  # Output: 8