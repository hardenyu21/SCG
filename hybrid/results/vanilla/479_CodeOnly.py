import random
import string
import pandas as pd

def task_func(data_list, seed=0):
    random.seed(seed)
    
    def replace_random_substring(s):
        # Split the string by commas to find potential substrings
        parts = s.split(',')
        # Choose a random part to replace
        if len(parts) > 1:
            index = random.randint(0, len(parts) - 1)
            # Generate a random string of the same length as the chosen part
            random_str = ''.join(random.choices(string.ascii_lowercase, k=len(parts[index])))
            # Replace the chosen part with the random string
            parts[index] = random_str
            return ','.join(parts)
        else:
            # If no commas, replace the whole string
            random_str = ''.join(random.choices(string.ascii_lowercase, k=len(s)))
            return random_str

    # Apply the replacement function to each string in the list
    modified_list = [replace_random_substring(s) for s in data_list]
    
    # Create a DataFrame with the original and modified strings
    df = pd.DataFrame({
        'Original String': data_list,
        'Modified String': modified_list
    })
    
    return df

# Example usage:
data_list = ["hello,world", "foo,bar,baz", "singleword"]
df = task_func(data_list)
print(df)