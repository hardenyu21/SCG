import pandas as pd
import itertools
import random

def task_func(colors, states):
    # Generate the Cartesian product of colors and states
    combinations = list(itertools.product(colors, states))
    
    # Shuffle the combinations
    random.shuffle(combinations)
    
    # Determine the number of columns for the DataFrame
    num_columns = min(len(colors), len(states))
    
    # Calculate the number of rows needed for each column
    num_rows = len(combinations) // num_columns
    remainder = len(combinations) % num_columns
    
    # Create a list to hold the data for each column
    column_data = []
    
    # Distribute the combinations into columns
    start_index = 0
    for i in range(num_columns):
        # Calculate the end index for the current column
        end_index = start_index + num_rows + (1 if i < remainder else 0)
        # Extract the combinations for the current column
        column_combinations = combinations[start_index:end_index]
        # Format the combinations as "Color:State"
        formatted_column = [f"{color}:{state}" for color, state in column_combinations]
        # Add the formatted column to the list
        column_data.append(formatted_column)
        # Update the start index for the next column
        start_index = end_index
    
    # Create the DataFrame from the column data
    df = pd.DataFrame(column_data).T
    
    return df

# Example usage:
colors = ['Red', 'Green', 'Blue']
states = ['California', 'Texas', 'New York', 'Florida']
df = task_func(colors, states)
print(df)