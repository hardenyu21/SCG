import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(file_path="data.csv", columns=["A", "B", "C"]):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    
    # Convert numeric values to floats
    for col in columns:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    
    # Plot the data
    fig, ax = plt.subplots()
    for col in columns:
        if col in df.columns:
            ax.plot(df[col], label=col)
    ax.set_title('Line Chart of Specified Columns')
    ax.set_xlabel('Index')
    ax.set_ylabel('Values')
    ax.legend()
    
    # Compute the cube-root of the data
    cube_root_series = df[columns].apply(np.cbrt)
    
    # Return the DataFrame, Axes, and Series
    return df, ax, cube_root_series

# Example usage:
# df, ax, cube_root_series = task_func("data.csv", ["A", "B", "C"])
# plt.show()