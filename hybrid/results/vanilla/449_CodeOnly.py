import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

def task_func(data: pd.DataFrame) -> (pd.DataFrame, list):
    # Initialize the StandardScaler
    scaler = StandardScaler()
    
    # Fit and transform the data
    standardized_data = scaler.fit_transform(data)
    
    # Convert the standardized data back to a DataFrame
    standardized_data = pd.DataFrame(standardized_data, columns=data.columns, index=data.index)
    
    # Create a list to store the Axes objects
    axes_list = []
    
    # Plot histograms for each feature
    for column in standardized_data.columns:
        fig, ax = plt.subplots()
        standardized_data[column].hist(bins=20, ax=ax)
        ax.set_title(f'Histogram of {column}')
        ax.set_xlabel('Value')
        ax.set_ylabel('Frequency')
        axes_list.append(ax)
    
    # Return the standardized data and the list of Axes objects
    return standardized_data, axes_list