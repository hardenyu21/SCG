import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def task_func(dataframe, target_value='332'):
    # Create a DataFrame with Boolean values indicating the presence of the target value
    bool_df = dataframe == target_value
    
    # Create a heatmap using seaborn
    plt.figure(figsize=(10, 8))
    ax = sns.heatmap(bool_df, cmap='viridis', cbar=False)
    
    # Set the title of the heatmap
    ax.set_title(f'Heatmap of occurrences of target value: {target_value}')
    
    # Show the plot
    plt.show()
    
    # Return the Boolean DataFrame and the Axes object
    return bool_df, ax

# Example usage:
# df = pd.DataFrame({
#     'A': [1, 2, 332, 4],
#     'B': [332, 5, 6, 7],
#     'C': [8, 9, 10, 332]
# })
# bool_df, ax = task_func(df, target_value=332)