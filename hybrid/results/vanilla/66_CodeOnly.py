import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Constants
COLUMNS = ['col1', 'col2', 'col3']

def task_func(data):
    # Step 1: Build a pandas DataFrame
    df = pd.DataFrame(data, columns=COLUMNS)
    
    # Step 2: Group the values in the column 'col3' by ['col1', 'col2']
    grouped_df = df.groupby(['col1', 'col2'])['col3'].mean().reset_index()
    
    # Step 3: Reset the index of the newly created dataframe
    grouped_df = grouped_df.reset_index(drop=True)
    
    # Step 4: Create a distribution plot of the 'col3' column
    plt.figure(figsize=(10, 6))
    ax = sns.histplot(grouped_df['col3'], kde=True)
    ax.set_xlabel('col3')
    
    # Return the DataFrame and the plot object
    return grouped_df, ax

# Example usage:
# data = [[1, 'A', 10], [1, 'A', 15], [2, 'B', 20], [2, 'B', 25]]
# df, ax = task_func(data)
# plt.show()