from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import pandas as pd

def task_func(df):
    # Replace missing values with the column's average
    df_filled = df.fillna(df.mean())
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Normalize the numeric columns
    df_normalized = pd.DataFrame(scaler.fit_transform(df_filled), columns=df.columns)
    
    # Create a box plot for each column
    ax = df_normalized.boxplot(figsize=(10, 6))
    plt.title('Box Plot of Normalized Columns')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Return the normalized DataFrame and the Axes object
    return df_normalized, ax

# Example usage:
# df = pd.DataFrame({
#     'A': [1, 2, 3, None, 5],
#     'B': [5, None, 1, 2, 3]
# })
# normalized_df, ax = task_func(df)
# plt.show()