import pandas as pd
import matplotlib.pyplot as plt

def task_func(input_dict, target_value):
    # Convert the input dictionary of lists to a DataFrame
    df = pd.DataFrame(input_dict)
    
    # Check if the DataFrame is empty
    if df.empty:
        return pd.Series(), None
    
    # Search for rows with cells equal to the provided target_value
    target_rows = df[df == target_value]
    
    # Count the occurrences of the target value per column
    counts = target_rows.count()
    
    # Plot the counts of such rows per column
    ax = counts.plot(kind='bar', title=f'Count of {target_value} per Column')
    ax.set_ylabel('Count')
    ax.set_xlabel('Columns')
    
    # Show the plot
    plt.show()
    
    return counts, ax

# Example usage:
# input_dict = {'A': [1, 2, 3, 4], 'B': [2, 3, 4, 5], 'C': [3, 4, 5, 6]}
# target_value = 3
# counts, ax = task_func(input_dict, target_value)