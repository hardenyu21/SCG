import pandas as pd
import random
import matplotlib.pyplot as plt

def task_func(num_rows=100, categories=["a", "b", "c", "d", "e"], random_seed=42):
    # Validate the number of rows
    if num_rows < 1:
        raise ValueError("num_rows must be at least 1.")
    
    # Set the random seed for reproducibility
    random.seed(random_seed)
    
    # Generate random data
    data = {
        'Category': [random.choice(categories) for _ in range(num_rows)],
        'Value': [random.randint(1, 100) for _ in range(num_rows)]
    }
    
    # Create a DataFrame
    df = pd.DataFrame(data)
    
    # Plot the bar chart
    category_counts = df['Category'].value_counts()
    ax = category_counts.plot(kind='bar', title='Category Counts')
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')
    
    # Show the plot
    plt.show()
    
    return df, ax

# Example usage:
# df, ax = task_func(num_rows=100, categories=["a", "b", "c", "d", "e"], random_seed=42)