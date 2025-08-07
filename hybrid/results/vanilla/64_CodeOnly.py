import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Constants
COLUMNS = ['col1', 'col2', 'col3']

def task_func(data):
    # Create a DataFrame from the input data
    df = pd.DataFrame(data, columns=COLUMNS)
    
    # Count the occurrences of each value in 'col3' grouped by 'col1' and 'col2'
    grouped_data = df.groupby(['col1', 'col2', 'col3']).size().unstack(fill_value=0)
    
    # Plot the heatmap
    plt.figure(figsize=(10, 8))
    ax = sns.heatmap(grouped_data, annot=True, fmt="d", cmap="YlGnBu", cbar_kws={'label': 'Count'})
    plt.title('Distribution of col3 values grouped by col1 and col2')
    plt.xlabel('col3')
    plt.ylabel('col1 and col2')
    
    # Return the DataFrame and the Axes object
    return grouped_data, ax

# Example usage:
# data = [
#     ['A', 'X', 1],
#     ['A', 'X', 2],
#     ['A', 'Y', 1],
#     ['B', 'X', 2],
#     ['B', 'Y', 1],
#     ['B', 'Y', 1]
# ]
# df, ax = task_func(data)
# plt.show()