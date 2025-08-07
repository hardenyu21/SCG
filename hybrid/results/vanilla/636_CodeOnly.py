import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Constants
COLUMNS = ['Column1', 'Column2', 'Column3', 'Column4', 'Column5']

def task_func(rows):
    # Generate a DataFrame with random integer values between 0 and 9
    df = pd.DataFrame(np.random.randint(0, 10, size=(rows, len(COLUMNS))), columns=COLUMNS)
    
    # Count the non-zero values in each column
    non_zero_counts = (df != 0).sum()
    
    # Create a bar plot
    fig, ax = plt.subplots()
    non_zero_counts.plot(kind='bar', ax=ax)
    ax.set_title('Non-Zero Values Count in Each Column')
    ax.set_xlabel('Columns')
    ax.set_ylabel('Count of Non-Zero Values')
    
    # Return the DataFrame and the Axes object
    return df, ax

# Example usage:
# df, ax = task_func(10)
# plt.show()