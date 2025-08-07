import pandas as pd
import itertools
from random import shuffle

def task_func(letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'], categories=['Category 1', 'Category 2', 'Category 3']):
    # Create a list of categories repeated enough times to match the number of letters
    repeated_categories = list(itertools.islice(itertools.cycle(categories), len(letters)))
    
    # Shuffle the categories to randomize the association
    shuffle(repeated_categories)
    
    # Create a DataFrame with the letters and their associated categories
    df = pd.DataFrame({
        'Letter': letters,
        'Category': repeated_categories
    })
    
    return df

# Example usage
df = task_func()
print(df)