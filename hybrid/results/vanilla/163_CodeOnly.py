import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def task_func(rows=5, cols=5):
    # Define the categories for the stacked bar chart
    categories = ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']
    
    # Check if the number of columns exceeds the number of available categories
    if cols > len(categories):
        raise ValueError("The number of columns exceeds the number of available categories.")
    
    # Generate random numerical data
    data = np.random.rand(rows, cols)
    
    # Create a DataFrame with the generated data
    df = pd.DataFrame(data, columns=categories[:cols])
    
    # Plot the stacked bar chart
    ax = df.plot(kind='bar', stacked=True, figsize=(10, 6))
    
    # Set labels and title
    ax.set_xlabel('Index')
    ax.set_ylabel('Values')
    ax.set_title('Stacked Bar Chart of Random Data')
    
    # Show the plot
    plt.tight_layout()
    plt.show()
    
    # Return the Axes object
    return ax

# Example usage:
# ax = task_func(rows=5, cols=3)