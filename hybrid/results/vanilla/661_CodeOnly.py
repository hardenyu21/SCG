import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Constants
LABELS = ['H\u2082O', 'O\u2082', 'CO\u2082', 'N\u2082', 'Ar']

def task_func(x, y, labels):
    # Create a DataFrame from the x and y values
    df = pd.DataFrame({'x': x, 'y': y})
    
    # Create a pivot table to prepare data for heatmap
    pivot_table = df.pivot_table(index='x', columns='y', aggfunc='size', fill_value=0)
    
    # Create a heatmap using seaborn
    plt.figure(figsize=(10, 8))
    ax = sns.heatmap(pivot_table, annot=True, fmt="d", cmap="YlGnBu", xticklabels=labels, yticklabels=labels)
    
    # Set labels and title
    ax.set_xlabel('Y Values')
    ax.set_ylabel('X Values')
    ax.set_title('Heatmap of X vs Y')
    
    # Show the plot
    plt.show()
    
    return ax, df

# Example usage
x = np.random.randint(0, 5, 100)
y = np.random.randint(0, 5, 100)
ax, df = task_func(x, y, LABELS)