from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def task_func(df):
    # Replace missing values with the column's average
    df_filled = df.fillna(df.mean())
    
    # Select numeric columns
    numeric_cols = df_filled.select_dtypes(include=['number']).columns
    
    # Standardize the numeric columns
    scaler = StandardScaler()
    df_filled[numeric_cols] = scaler.fit_transform(df_filled[numeric_cols])
    
    # Calculate the correlation matrix
    corr_matrix = df_filled.corr()
    
    # Plot the heatmap
    plt.figure(figsize=(10, 8))
    ax = sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Matrix Heatmap')
    plt.show()
    
    return df_filled, ax

# Example usage:
# df = pd.DataFrame({
#     'A': [1, 2, 3, None, 5],
#     'B': [5, None, 1, 3, 2],
#     'C': [None, 1, 2, 3, 4]
# })
# standardized_df, heatmap_ax = task_func(df)