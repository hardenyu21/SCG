import pandas as pd
import matplotlib.pyplot as plt

def task_func(df, dct, columns=None, plot_histograms=False):
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input df is not a DataFrame.")
    
    # Replace values in the DataFrame using the dictionary mapping
    df_replaced = df.replace(dct)
    
    # Rename columns to 'col1', 'col2', etc.
    df_replaced.columns = [f'col{i+1}' for i in range(len(df_replaced.columns))]
    
    # Plot histograms for specified columns if requested
    if plot_histograms and columns is not None:
        for col in columns:
            if col in df_replaced.columns:
                plt.figure()
                df_replaced[col].hist()
                plt.title(f'Histogram of {col}')
                plt.xlabel(col)
                plt.ylabel('Frequency')
                plt.show()
    
    return df_replaced