import pandas as pd
import matplotlib.pyplot as plt

def task_func(data, column_name="target_column"):
    # Convert JSON data to a Pandas DataFrame
    df = pd.DataFrame(data)
    
    # Check if the specified column exists in the DataFrame
    if column_name not in df.columns:
        raise ValueError(f"The specified column '{column_name}' does not exist in the DataFrame.")
    
    # Convert non-numeric columns to categorical and then to numeric codes
    if not pd.api.types.is_numeric_dtype(df[column_name]):
        df[column_name] = pd.Categorical(df[column_name]).codes
    
    # Plot the histogram
    fig, ax = plt.subplots()
    ax.hist(df[column_name], bins=10, edgecolor='black')
    ax.set_title(f'Histogram of {column_name}')
    ax.set_xlabel(column_name)
    ax.set_ylabel('Frequency')
    
    # Show the plot
    plt.show()
    
    return df, ax