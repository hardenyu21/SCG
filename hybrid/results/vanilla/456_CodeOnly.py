import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler

def task_func(data: pd.DataFrame) -> (pd.DataFrame, plt.Axes):
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler(feature_range=(0, 1))
    
    # Fit and transform the data to normalize it
    normalized_data = scaler.fit_transform(data)
    
    # Create a DataFrame from the normalized data
    normalized_df = pd.DataFrame(normalized_data, columns=data.columns, index=data.index)
    
    # Create a heatmap using seaborn
    plt.figure(figsize=(10, 8))
    ax = sns.heatmap(normalized_df, cmap="YlGnBu", cbar_kws={'label': 'Normalized Value'})
    
    # Set the title of the heatmap
    ax.set_title('Normalized Data Heatmap')
    
    # Return the normalized DataFrame and the Axes object
    return normalized_df, ax

# Example usage:
# df = pd.DataFrame({
#     'A': [1, 2, 3],
#     'B': [4, 5, 6],
#     'C': [7, 8, 9]
# })
# normalized_df, ax = task_func(df)
# plt.show()