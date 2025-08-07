import pandas as pd
import numpy as np

def task_func(days, random_seed=0):
    # Set the random seed for reproducibility
    np.random.seed(random_seed)
    
    # Create a date range starting from '2023-01-01' for the specified number of days
    date_range = pd.date_range(start='2023-01-01', periods=days)
    
    # Generate random spending data for each category
    groceries = np.random.randint(0, 101, size=days)
    entertainment = np.random.randint(0, 101, size=days)
    rent = np.random.randint(0, 101, size=days)
    utilities = np.random.randint(0, 101, size=days)
    miscellaneous = np.random.randint(0, 101, size=days)
    
    # Create a DataFrame with the generated data
    df = pd.DataFrame({
        'Groceries': groceries,
        'Entertainment': entertainment,
        'Rent': rent,
        'Utilities': utilities,
        'Miscellaneous': miscellaneous
    }, index=date_range)
    
    return df

# Example usage:
# df = task_func(10)
# print(df)