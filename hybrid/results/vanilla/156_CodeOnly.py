import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

def task_func(data):
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Fit and transform the data using MinMaxScaler
    normalized_data = scaler.fit_transform(data)
    
    # Create a DataFrame from the normalized data
    df_normalized = pd.DataFrame(normalized_data, columns=data.columns)
    
    # Calculate the average of each row and add it as a new column 'Average'
    df_normalized['Average'] = df_normalized.mean(axis=1)
    
    # Plot the averages
    fig, ax = plt.subplots()
    ax.bar(df_normalized.index, df_normalized['Average'])
    ax.set_title('Average of Each Row')
    ax.set_xlabel('Row Index')
    ax.set_ylabel('Average Value')
    
    # Show the plot
    plt.show()
    
    # Return the DataFrame and the Axes object
    return df_normalized, ax