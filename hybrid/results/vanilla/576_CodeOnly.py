from random import shuffle, randint
import pandas as pd

def task_func(l, n_groups=5):
    # Shuffle the list
    shuffle(l)
    
    # Create a longer series by cycling through the shuffled list
    series_length = len(l) * n_groups
    cycled_list = (l * n_groups)[:series_length]
    
    # Create a pandas Series from the cycled list
    series = pd.Series(cycled_list)
    
    # Function to modify each element by moving n characters from the start to the end
    def modify_string(s):
        n = randint(1, len(s))  # Randomly select n characters
        return s[n:] + s[:n]
    
    # Apply the modification to each element in the series
    modified_series = series.apply(modify_string)
    
    return modified_series

# Example usage:
# l = ["apple", "banana", "cherry"]
# print(task_func(l, n_groups=3))