import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

# Constants
PLOT_TITLE = "Scaled Values"

def task_func(data_dict):
    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(data_dict)
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Fit and transform the data
    scaled_data = scaler.fit_transform(df)
    
    # Create a DataFrame with the scaled data
    scaled_df = pd.DataFrame(scaled_data, columns=df.columns)
    
    # Plot the scaled data
    ax = scaled_df.plot(kind='line', title=PLOT_TITLE)
    ax.set_xlabel('Index')
    ax.set_ylabel('Scaled Value')
    plt.grid(True)
    plt.show()
    
    # Return the scaled DataFrame and the Axes object
    return scaled_df, ax

# Example usage:
# data_dict = {'feature1': [1, 2, 3, 4, 5], 'feature2': [5, 4, 3, 2, 1]}
# scaled_df, ax = task_func(data_dict)