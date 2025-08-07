import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

def task_func(data_dict, data_keys):
    # Check if any of the keys in data_keys are present in data_dict
    if not any(key in data_dict for key in data_keys):
        raise ValueError("No keys in `data_keys` are found in `data_dict`.")
    
    # Extract the data for the specified keys
    data = {key: data_dict[key] for key in data_keys if key in data_dict}
    
    # Create a DataFrame from the extracted data
    df = pd.DataFrame(data)
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Fit and transform the data
    normalized_data = scaler.fit_transform(df)
    
    # Create a DataFrame with the normalized data
    normalized_df = pd.DataFrame(normalized_data, columns=df.columns)
    
    # Plot the normalized data
    ax = normalized_df.plot(kind='line', title='Normalized Data')
    ax.set_xlabel('Index')
    ax.set_ylabel('Normalized Value')
    
    # Show the plot
    plt.show()
    
    # Return the normalized DataFrame and the Axes object
    return normalized_df, ax