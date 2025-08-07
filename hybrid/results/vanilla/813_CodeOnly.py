from itertools import combinations
import pandas as pd

def task_func(number_list, element):
    # Check if the list is empty
    if not number_list:
        return pd.DataFrame(columns=['Combinations'])
    
    # Find all unique combinations of 3 numbers
    comb = combinations(number_list, 3)
    
    # Filter combinations that add up to the given element
    valid_combinations = [c for c in comb if sum(c) == element]
    
    # Create a DataFrame with the valid combinations
    df = pd.DataFrame(valid_combinations, columns=['Combinations'])
    
    return df

# Example usage:
result = task_func([-1, 1, 0, -2, 2, 3], 0)
print(result)

result = task_func([], 0)
print(result)