import pandas as pd
import matplotlib.pyplot as plt
from itertools import cycle

def task_func(df, groups=['A', 'B', 'C', 'D', 'E']):
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input 'df' must be a pandas DataFrame.")
    
    # Check if the required columns are present
    required_columns = ['date', 'value', 'group']
    if not all(column in df.columns for column in required_columns):
        raise ValueError("DataFrame must contain 'date', 'value', and 'group' columns.")
    
    # Convert 'date' column to ordinal
    df['date_ordinal'] = df['date'].apply(lambda x: x.toordinal())
    
    # Create a color cycle for different groups
    colors = cycle(plt.cm.tab10.colors)
    
    # Create a scatter plot
    fig, ax = plt.subplots()
    for group in groups:
        group_data = df[df['group'] == group]
        if not group_data.empty:
            ax.scatter(group_data['date_ordinal'], group_data['value'], color=next(colors), label=group)
    
    # Set plot title and labels
    ax.set_title('Scatterplot of Values for Each Group Over Time')
    ax.set_xlabel('Date (ordinal)')
    ax.set_ylabel('Value')
    ax.legend(title='Group')
    
    # Show the plot
    plt.show()
    
    return ax