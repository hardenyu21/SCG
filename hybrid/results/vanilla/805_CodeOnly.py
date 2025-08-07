import pandas as pd
import random

def task_func(dictionary, item, seed):
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # Convert the dictionary to a pandas DataFrame
    df = pd.DataFrame(dictionary)
    
    # Find the locations of the item in the DataFrame
    locations = []
    for col in df.columns:
        for idx, value in enumerate(df[col]):
            if value == item:
                locations.append((idx, col))
    
    # Count the number of occurrences of the item
    count = len(locations)
    
    # Add a random integer x, where 0 <= x < 10, to the count
    random_number = random.randint(0, 9)
    count_with_random = count + random_number
    
    return locations, count_with_random, df

# Example usage
dict_data = {'A': ['a', 'b', 'e'], 'B': ['c', 'd', 'd'], '2': ['asdf', 'ddd', 'aaaa'], '12': ['e', 'e', 'd']}
result = task_func(dict_data, 'e', seed=2)
print(result)