import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import pandas as pd

def task_func(df):
    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError("The DataFrame is empty.")
    
    # Select only numeric columns
    numeric_df = df.select_dtypes(include=[np.number])
    
    # Check if there are no numeric columns
    if numeric_df.empty:
        raise ValueError("No numeric columns are present in the DataFrame.")
    
    # Standardize the numeric columns
    scaler = StandardScaler()
    standardized_data = scaler.fit_transform(numeric_df)
    standardized_df = pd.DataFrame(standardized_data, columns=numeric_df.columns, index=numeric_df.index)
    
    # Compute the correlation matrix
    corr_matrix = standardized_df.corr()
    
    # Plot the heatmap
    plt.figure(figsize=(10, 8))
    heatmap = sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Matrix Heatmap')
    plt.close()  # Close the plot to prevent it from displaying immediately
    
    return standardized_df, heatmap.get_figure()