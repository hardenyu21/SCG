import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(df):
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame.")
    
    # Check if the required columns are present
    required_columns = {'Date', 'Time', 'Temperature'}
    if not required_columns.issubset(df.columns):
        raise ValueError("DataFrame must contain 'Date', 'Time', and 'Temperature' columns.")
    
    # Convert 'Date' and 'Time' to a single datetime column
    df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'])
    
    # Pivot the DataFrame to have 'Date' as index, 'Time' as columns, and 'Temperature' as values
    pivot_df = df.pivot(index='Date', columns='Time', values='Temperature')
    
    # Create a heatmap using seaborn
    plt.figure(figsize=(12, 8))
    ax = sns.heatmap(pivot_df, cmap='coolwarm', annot=True, fmt=".1f", cbar_kws={'label': 'Temperature (°C)'})
    
    # Set labels and title
    ax.set_xlabel('Time')
    ax.set_ylabel('Date')
    ax.set_title('Temperature Heatmap')
    
    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)
    
    # Adjust layout
    plt.tight_layout()
    
    # Return the Axes object
    return ax