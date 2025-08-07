import pandas as pd
from random import shuffle

# Constants
POSSIBLE_VALUES = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

def task_func(list_of_lists):
    dataframes = []
    for sublist in list_of_lists:
        # Shuffle the POSSIBLE_VALUES for each DataFrame
        shuffled_values = POSSIBLE_VALUES[:]
        shuffle(shuffled_values)
        
        # Create a dictionary where each key is a column name and each value is the shuffled list
        data = {column_name: shuffled_values for column_name in sublist}
        
        # Create a DataFrame from the dictionary
        df = pd.DataFrame(data)
        
        # Append the DataFrame to the list
        dataframes.append(df)
    
    return dataframes

# Example usage:
list_of_lists = [['Col1', 'Col2'], ['ColA', 'ColB', 'ColC'], ['X', 'Y']]
dataframes = task_func(list_of_lists)
for df in dataframes:
    print(df)