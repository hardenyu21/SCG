import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

def task_func(df):
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler(feature_range=(0, 1))
    
    # Function to scale a group
    def scale_group(group):
        # Scale the 'Age' and 'Income' columns
        group[['Age', 'Income']] = scaler.fit_transform(group[['Age', 'Income']])
        return group
    
    # Apply the scaling function to each group by 'id'
    scaled_df = df.groupby('id').apply(scale_group).reset_index(drop=True)
    
    # Create a histogram of the 'Income' column after scaling
    plt.figure(figsize=(10, 6))
    plt.hist(scaled_df['Income'], bins=30, alpha=0.7, color='blue', edgecolor='black')
    plt.title('Histogram of Scaled Income')
    plt.xlabel('Scaled Income')
    plt.ylabel('Frequency')
    plt.grid(True)
    
    # Get the histogram data
    histogram_data, bin_edges = np.histogram(scaled_df['Income'], bins=30)
    
    # Return the scaled DataFrame and the histogram data
    return scaled_df, histogram_data

# Example usage:
# df = pd.DataFrame({
#     'id': [1, 1, 2, 2, 3, 3],
#     'Age': [25, 30, 35, 40, 45, 50],
#     'Income': [50000, 60000, 70000, 80000, 90000, 100000]
# })
# scaled_df, histogram_data = task_func(df)
# print(scaled_df)
# print(histogram_data)