import pandas as pd
import numpy as np
from collections import Counter
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(df: pd.DataFrame) -> (Counter, plt.Axes):
    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError("The DataFrame is empty.")
    
    # Check if 'name' and 'age' columns are present
    if 'name' not in df.columns or 'age' not in df.columns:
        raise ValueError("DataFrame must contain 'name' and 'age' columns.")
    
    # Round down ages to the nearest integer and ensure they are not negative
    df['age'] = df['age'].apply(lambda x: int(np.floor(x)))
    if (df['age'] < 0).any():
        raise ValueError("Age must not be negative.")
    
    # Identify duplicate names
    duplicates = df[df.duplicated('name', keep=False)]
    
    # If there are no duplicates, return an empty Counter and None for the plot
    if duplicates.empty:
        return Counter(), None
    
    # Record the age distribution for duplicate names
    age_distribution = Counter(duplicates['age'])
    
    # Plot the histogram of age distribution
    plt.figure(figsize=(8, 6))
    ax = sns.histplot(duplicates['age'], bins=np.arange(duplicates['age'].min() - 0.5, duplicates['age'].max() + 1.5, 1), kde=False)
    ax.set_title('Age Distribution of Duplicate Names')
    ax.set_xlabel('Age')
    ax.set_ylabel('Count')
    
    # Return the Counter and the Axes object
    return age_distribution, ax