import numpy as np
import matplotlib.pyplot as plt

# Constants
COLORS = ['r', 'g', 'b']

def task_func(df, group_col, value_col, group_name):
    # Check if the group_name exists in the dataframe
    if group_name not in df[group_col].unique():
        raise ValueError(f"The group_name '{group_name}' does not exist in the dataframe.")
    
    # Filter the dataframe for the specific group
    group_df = df[df[group_col] == group_name]
    
    # Create a bar plot
    fig, ax = plt.subplots()
    ax.bar(group_df[group_col], group_df[value_col], color=COLORS[:len(group_df)])
    
    # Set the title and labels
    ax.set_title(f'Bar chart of {value_col} for {group_name}')
    ax.set_xlabel(group_col)
    ax.set_ylabel(value_col)
    
    # Return the axes object
    return ax