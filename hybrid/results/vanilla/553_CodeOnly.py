import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Constants
COLUMNS = ['A', 'B', 'C', 'D', 'E']

def task_func(a, b):
    # Determine the number of columns based on the length of list 'b'
    num_columns = len(b)
    
    # Select the appropriate column names from the COLUMNS list
    selected_columns = COLUMNS[:num_columns]
    
    # Generate random values for the DataFrame
    data = np.random.rand(len(a), num_columns)
    
    # Create the DataFrame with 'a' as the index and selected columns
    df = pd.DataFrame(data, index=a, columns=selected_columns)
    
    # Plot the DataFrame as a bar chart
    ax = df.plot(kind='bar', figsize=(10, 6))
    
    # Set labels and title
    ax.set_xlabel('Index')
    ax.set_ylabel('Values')
    ax.set_title('Bar Chart of Random Values')
    
    # Show the plot
    plt.tight_layout()
    plt.show()
    
    # Return the Axes object
    return ax

# Example usage:
# a = ['Row1', 'Row2', 'Row3']
# b = [1, 2, 3]  # Length determines the number of columns
# task_func(a, b)