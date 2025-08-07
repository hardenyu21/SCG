import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

def task_func(df):
    # Check if the input is a DataFrame and if it is not empty
    if not isinstance(df, pd.DataFrame) or df.empty:
        raise ValueError("Input must be a non-empty DataFrame.")
    
    # Extract the last column name
    last_column_name = df.columns[-1]
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Reshape the last column for scaling
    last_column = df[last_column_name].values.reshape(-1, 1)
    
    # Fit and transform the last column
    normalized_last_column = scaler.fit_transform(last_column)
    
    # Create a new DataFrame with the normalized last column
    df_normalized = df.copy()
    df_normalized[last_column_name] = normalized_last_column
    
    # Plot the normalized data
    fig, ax = plt.subplots()
    ax.plot(df_normalized.index, df_normalized[last_column_name], label='Normalized Value')
    ax.set_title(f'Normalized Data of {last_column_name}')
    ax.set_xlabel('Index')
    ax.set_ylabel('Normalized Value')
    ax.legend()
    
    # Return the normalized DataFrame and the Axes object
    return df_normalized, ax