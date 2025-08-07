import pandas as pd
from collections import Counter

def task_func(df):
    # Create a 'combination' column by joining elements in each row
    df['combination'] = df.apply(lambda row: tuple(row), axis=1)
    
    # Calculate the frequency of each combination
    combination_counts = Counter(df['combination'])
    
    # Convert the Counter object to a dictionary
    combination_frequency = dict(combination_counts)
    
    return combination_frequency

# Example usage:
# df = pd.DataFrame({
#     'A': [1, 2, 1, 2],
#     'B': [3, 4, 3, 4],
#     'C': [5, 6, 5, 6]
# })
# print(task_func(df))