import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def task_func(file_path: str, plot_path: str) -> (float, float, str):
    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The CSV file at '{file_path}' does not exist.")
    
    # Read the CSV file
    try:
        data = pd.read_csv(file_path)
    except Exception as e:
        raise ValueError(f"Error reading the CSV file: {e}")
    
    # Clean the data: select numeric columns
    numeric_data = data.select_dtypes(include=[np.number])
    
    # Flatten the data to a single series if it has multiple columns
    if not numeric_data.empty:
        numeric_data = numeric_data.stack()
    
    # Calculate mean and median
    mean_value = numeric_data.mean() if not numeric_data.empty else np.nan
    median_value = numeric_data.median() if not numeric_data.empty else np.nan
    
    # Generate a plot
    plt.figure(figsize=(10, 6))
    plt.plot(numeric_data.index, numeric_data.values, marker='o', linestyle='-')
    plt.title("Data Visualization")
    plt.xlabel("Index")
    plt.ylabel("Value")
    
    # Save the plot
    plt.savefig(plot_path)
    plt.close()
    
    return mean_value, median_value, plot_path