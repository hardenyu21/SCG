import numpy as np
import matplotlib.pyplot as plt
import os

def task_func(mystrings, folder_path, seed=None):
    # Deduplicate mystrings while maintaining original order
    seen = set()
    deduplicated_strings = []
    for s in mystrings:
        if s not in seen:
            seen.add(s)
            deduplicated_strings.append(s)
    
    # Set the random seed for reproducibility if provided
    if seed is not None:
        np.random.seed(seed)
    
    # Ensure the directory exists
    try:
        os.makedirs(folder_path, exist_ok=True)
    except Exception as e:
        raise FileNotFoundError(f"Could not create directory {folder_path}: {e}")
    
    # Generate and save bar charts
    saved_files = []
    for plot_name in deduplicated_strings:
        # Generate 10 random data points in [0, 1)
        data = np.random.rand(10)
        
        # Create a bar chart
        plt.figure()
        plt.bar(range(10), data)
        plt.title(plot_name)
        plt.xlabel('Index')
        plt.ylabel('Value')
        
        # Save the plot
        file_name = f"{plot_name.replace(' ', '_')}.png"
        file_path = os.path.join(folder_path, file_name)
        plt.savefig(file_path)
        plt.close()
        
        # Add the file name to the list of saved files
        saved_files.append(file_name)
    
    return saved_files