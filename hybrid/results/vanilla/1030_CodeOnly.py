import itertools
import string
import pandas as pd

def task_func():
    # Generate all possible combinations with replacement of three letters
    combinations = itertools.combinations_with_replacement(string.ascii_lowercase, 3)
    
    # Convert combinations to a list of strings
    combination_list = [''.join(combination) for combination in combinations]
    
    # Create a DataFrame from the list
    df = pd.DataFrame(combination_list, columns=['Combination'])
    
    return df

# Example usage
df = task_func()
print(df)