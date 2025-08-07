import pandas as pd
import itertools
import numpy as np

def task_func(animals=None, foods=None):
    # Predefined lists for special cases
    default_animals = ['Dog', 'Cat', 'Bird', 'Fish']
    default_foods = ['Bones', 'Fish', 'Seeds', 'Pellets']
    
    # Handle special cases where lists are empty or not provided
    if animals is None or len(animals) == 0:
        animals = default_animals
    if foods is None or len(foods) == 0:
        foods = default_foods
    
    # Generate all possible combinations of animals and foods
    combinations = list(itertools.product(animals, foods))
    
    # Shuffle the combinations to ensure variety
    np.random.shuffle(combinations)
    
    # Create a DataFrame from the combinations
    df = pd.DataFrame(combinations, columns=['Animal', 'Food'])
    
    # Format each cell as 'animal:food'
    df['Animal:Food'] = df.apply(lambda row: f"{row['Animal']}:{row['Food']}", axis=1)
    
    # Pivot the DataFrame to have animals as rows and foods as columns
    df_pivot = df.pivot(index='Animal', columns='Food', values='Animal:Food')
    
    # Reset the index to make 'Animal' a column again
    df_pivot.reset_index(inplace=True)
    
    # Fill NaN values with empty strings
    df_pivot.fillna('', inplace=True)
    
    return df_pivot

# Example usage:
# df = task_func(['Dog', 'Cat'], ['Bones', 'Fish'])
# print(df)