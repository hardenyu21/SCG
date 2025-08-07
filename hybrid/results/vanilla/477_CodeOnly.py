import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def task_func(N=100, CATEGORIES=["A", "B", "C", "D", "E"], seed=42):
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Generate random values for columns "x" and "y"
    x = np.random.rand(N)
    y = np.random.rand(N)
    
    # Ensure each category appears at least once if N >= len(CATEGORIES)
    if N >= len(CATEGORIES):
        # Randomly sample categories with replacement
        category = np.random.choice(CATEGORIES, N)
        # Ensure each category appears at least once
        unique_categories = np.random.choice(CATEGORIES, len(CATEGORIES), replace=False)
        # Replace the first occurrences with unique categories
        for i, cat in enumerate(unique_categories):
            category[i] = cat
    else:
        # Randomly sample categories without replacement
        category = np.random.choice(CATEGORIES, N, replace=False)
    
    # Create the DataFrame
    df = pd.DataFrame({'x': x, 'y': y, 'category': category})
    
    # Create a scatter plot
    fig, ax = plt.subplots()
    scatter = ax.scatter(df['x'], df['y'], c=df['category'].astype('category').cat.codes, cmap='viridis')
    
    # Add a legend
    legend1 = ax.legend(*scatter.legend_elements(), title="Categories")
    ax.add_artist(legend1)
    
    # Show the plot
    plt.show()
    
    # Return the DataFrame and the Axes object
    return df, ax

# Example usage
df, ax = task_func(N=100, CATEGORIES=["A", "B", "C", "D", "E"], seed=42)