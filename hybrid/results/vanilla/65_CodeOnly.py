import pandas as pd
import matplotlib.pyplot as plt

COLUMNS = ['col1', 'col2', 'col3']

def task_func(data):
    # Create a DataFrame from the list of elements
    df = pd.DataFrame(data, columns=COLUMNS)
    
    # Group by all columns except the last one and aggregate the last column
    grouped_df = df.groupby(COLUMNS[:-1])[COLUMNS[-1]].sum().reset_index()
    
    # Create a line chart
    fig, ax = plt.subplots()
    for name, group in grouped_df.groupby(COLUMNS[:-1]):
        ax.plot(group.index, group[COLUMNS[-1]], marker='o', label=str(name))
    
    # Set the x-label and y-label
    x_label = '-'.join(COLUMNS[:-1])
    y_label = COLUMNS[-1]
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    
    # Add a legend
    ax.legend(title='-'.join(COLUMNS[:-1]))
    
    # Show the plot
    plt.show()
    
    return grouped_df, ax

# Example usage:
# data = [
#     ['A', 'X', 10],
#     ['A', 'X', 20],
#     ['B', 'Y', 15],
#     ['B', 'Y', 25]
# ]
# df, ax = task_func(data)