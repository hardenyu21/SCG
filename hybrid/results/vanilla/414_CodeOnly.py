import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(data, column="c"):
    # Convert the data dictionary to a DataFrame
    df = pd.DataFrame(data)
    
    # Remove the specified column if it exists
    if column in df.columns:
        df = df.drop(columns=[column])
    
    # Check if there is any numeric data left to plot
    numeric_df = df.select_dtypes(include=[np.number])
    
    # Plot the numeric data if it exists
    ax = None
    if not numeric_df.empty:
        ax = numeric_df.plot(kind='line', figsize=(10, 6))
        plt.title('Plot of Numeric Data')
        plt.xlabel('Index')
        plt.ylabel('Values')
        plt.grid(True)
        plt.show()
    
    return df, ax