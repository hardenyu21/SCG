import pandas as pd
import string

def task_func(word):
    # Check if the input word is in lowercase and contains only alphabetic characters
    if not word.islower() or not word.isalpha():
        raise ValueError("The input word must be in lowercase and contain only alphabetic characters.")
    
    # Create a list of tuples containing each letter and its 1-based position in the alphabet
    data = [(letter, string.ascii_lowercase.index(letter) + 1) for letter in word]
    
    # Create a DataFrame from the list of tuples
    df = pd.DataFrame(data, columns=['Letter', 'Position'])
    
    return df

# Example usage:
# df = task_func('zoo')
# print(df)