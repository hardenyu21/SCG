import pandas as pd
import matplotlib.pyplot as plt

def task_func(array):
    # Define the column names
    COLUMNS = ['A', 'B', 'C', 'D', 'E']
    
    # Create a DataFrame from the 2D list
    df = pd.DataFrame(array, columns=COLUMNS)
    
    # Calculate the sum of each column
    column_sums = df.sum()
    
    # Plot the sum of each column
    ax = column_sums.plot(kind='bar', title='Sum of Each Column')
    ax.set_ylabel('Sum')
    ax.set_xlabel('Columns')
    
    # Show the plot
    plt.show()
    
    # Return the DataFrame and the Axes object
    return df, ax

# Example usage:
# array = [
#     [1, 2, 3, 4, 5],
#     [5, 4, 3, 2, 1],
#     [2, 3, 4, 5, 6]
# ]
# df, ax = task_func(array)