import pandas as pd
from random import sample, seed

def task_func(dictionary, item, sample_size=None, random_seed=None):
    # Convert the dictionary to a pandas DataFrame
    df = pd.DataFrame.from_dict(dictionary, orient='index').transpose()
    
    # Find the positions of the item in the DataFrame
    positions = []
    for row_idx, row in df.iterrows():
        for col_idx, value in enumerate(row):
            if value == item:
                positions.append((row_idx, col_idx))
    
    # Record the frequency distribution of the item
    frequency_distribution = df.apply(lambda x: (x == item).sum()).to_dict()
    
    # Optionally return a random sample of these positions
    if sample_size is not None:
        if random_seed is not None:
            seed(random_seed)
        positions = sample(positions, min(sample_size, len(positions)))
    
    return positions, df, frequency_distribution

# Example usage
dictionary = {
    1: ['road', 'car', 'traffic'],
    2: ['car', 'light', 'candle']
}

positions, df, frequency_distribution = task_func(dictionary, 'car')
print("Positions:", positions)
print("DataFrame:\n", df)
print("Frequency Distribution:", frequency_distribution)