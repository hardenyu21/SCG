import pandas as pd
import time

# Constants
LETTERS = list('abcdefghijklmnopqrstuvwxyz')

def task_func(data, letter):
    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(data)
    
    # Filter rows where the 'Name' column values start with the specified letter
    filtered_df = df[df['Name'].str.startswith(letter, na=False)]
    
    # Return the filtered 'Name' column as a Series
    return filtered_df['Name']

# Example usage:
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'Age': [25, 30, 35, 40, 45, 50]
}

# Filter names starting with 'A'
filtered_names = task_func(data, 'A')
print(filtered_names)