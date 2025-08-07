import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Constants
COLUMNS = ['Date', 'Value']

def task_func(df, plot=False):
    # Check for required columns
    if not all(column in df.columns for column in COLUMNS):
        raise KeyError("DataFrame must contain 'Date' and 'Value' columns.")
    
    # Convert 'Date' column to datetime and set it as the index
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    
    # Split the 'Value' column into separate columns
    value_df = df['Value'].apply(pd.Series)
    
    # Scale the values using StandardScaler
    scaler = StandardScaler()
    scaled_values = scaler.fit_transform(value_df)
    
    # Create a DataFrame with the scaled values
    scaled_df = pd.DataFrame(scaled_values, index=df.index, columns=[f'Value_{i}' for i in range(value_df.shape[1])])
    
    # Plot the scaled values if plot is True
    ax = None
    if plot:
        ax = scaled_df.plot(kind='bar', figsize=(10, 6))
        ax.set_title("Scaled Values Over Time")
        ax.set_xlabel("Date")
        ax.set_ylabel("Scaled Value")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    
    return scaled_df, ax