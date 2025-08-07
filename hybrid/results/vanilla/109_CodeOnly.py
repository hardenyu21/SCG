import pandas as pd
import matplotlib.pyplot as plt

def task_func(df, items=None, locations=None):
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input 'df' must be a pandas DataFrame.")
    
    # Check if 'Item' and 'Location' columns are present
    if 'Item' not in df.columns or 'Location' not in df.columns:
        raise ValueError("DataFrame must contain 'Item' and 'Location' columns.")
    
    # Define default lists if none are provided
    if items is None:
        items = ['Item1', 'Item2', 'Item3']  # Example default items
    if locations is None:
        locations = ['LocationA', 'LocationB', 'LocationC']  # Example default locations
    
    # Filter the DataFrame to include only specified items and locations
    filtered_df = df[df['Item'].isin(items) & df['Location'].isin(locations)]
    
    # Count the occurrences of each item per location
    item_location_counts = filtered_df.groupby(['Location', 'Item']).size().unstack(fill_value=0)
    
    # Plot the bar chart
    ax = item_location_counts.plot(kind='bar', stacked=True, figsize=(10, 6))
    ax.set_title('Distribution of Items Across Locations')
    ax.set_xlabel('Location')
    ax.set_ylabel('Count')
    ax.legend(title='Item')
    
    # Show the plot
    plt.tight_layout()
    plt.show()
    
    return ax