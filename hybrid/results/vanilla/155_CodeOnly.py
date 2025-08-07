import pandas as pd
import matplotlib.pyplot as plt

# Constants
COLUMN_NAMES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

def task_func(data):
    # Create a DataFrame from the provided 2D array
    df = pd.DataFrame(data, columns=COLUMN_NAMES)
    
    # Compute the average of each row
    row_averages = df.mean(axis=1)
    
    # Append the averages as a new column in the DataFrame
    df['Average'] = row_averages
    
    # Plot the averages against their respective row indices
    fig, ax = plt.subplots()
    ax.plot(df.index, row_averages, marker='o', linestyle='-')
    ax.set_title('Row Averages')
    ax.set_xlabel('Row Index')
    ax.set_ylabel('Average')
    
    # Return the DataFrame and the Axes object
    return df, ax

# Example usage:
# data = [
#     [1, 2, 3, 4, 5, 6, 7, 8],
#     [8, 7, 6, 5, 4, 3, 2, 1],
#     [2, 3, 4, 5, 6, 7, 8, 9]
# ]
# df, ax = task_func(data)
# plt.show()