import pandas as pd
import random

def task_func(data, columns=['Name', 'Age', 'Occupation'], fill_missing=False, num_range=(0, 100), seed=None):
    # Set the random seed if provided
    if seed is not None:
        random.seed(seed)
    
    # Create a list of dictionaries from the data
    records = []
    for row in data:
        record = {columns[i]: value for i, value in enumerate(row)}
        records.append(record)
    
    # Create a DataFrame from the list of dictionaries
    df = pd.DataFrame(records, columns=columns)
    
    # Fill missing values if fill_missing is True
    if fill_missing:
        for col in columns:
            if df[col].isnull().any():
                if pd.api.types.is_numeric_dtype(df[col]):
                    # Fill numeric missing values with random numbers in the specified range
                    df[col].fillna(random.randint(*num_range), inplace=True)
                else:
                    # Fill non-numeric missing values with None
                    df[col].fillna(None, inplace=True)
    
    return df

# Example usage
data = [('Mango', 20), ('Apple', ), ('Banana', )]
df = task_func(data, columns=['Fruit', 'Quantity'], fill_missing=False, seed=42)
print(df)