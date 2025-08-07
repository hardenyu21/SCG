import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def task_func(file_location, sheet_name):
    # Check if the file exists
    if not os.path.exists(file_location):
        raise FileNotFoundError(f"The file does not exist at the specified path: {file_location}")
    
    # Load the Excel file
    try:
        df = pd.read_excel(file_location, sheet_name=sheet_name)
    except ValueError:
        raise ValueError(f"The specified sheet '{sheet_name}' does not exist in the workbook.")
    
    # Calculate mean and standard deviation for each column
    stats = {}
    for column in df.columns:
        mean_value = df[column].mean()
        std_value = df[column].std()
        stats[column] = {'mean': mean_value, 'std': std_value}
    
    # Create a bar chart
    fig, ax = plt.subplots()
    bar_width = 0.35
    index = np.arange(len(df.columns))
    
    means = [stats[col]['mean'] for col in df.columns]
    stds = [stats[col]['std'] for col in df.columns]
    
    bars1 = ax.bar(index, means, bar_width, label='Mean')
    bars2 = ax.bar(index + bar_width, stds, bar_width, label='Standard Deviation')
    
    ax.set_xlabel('Columns')
    ax.set_ylabel('Values')
    ax.set_title('Mean and Standard Deviation')
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(df.columns)
    ax.legend()
    
    plt.tight_layout()
    
    return stats, fig