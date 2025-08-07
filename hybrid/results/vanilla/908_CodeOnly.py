import os
import pandas as pd
import re
import matplotlib.pyplot as plt

def task_func(directory: str, pattern: str) -> list:
    # Compile the regular expression pattern for matching
    regex = re.compile(pattern)
    
    # List to store the Axes objects
    axes_list = []
    
    # Iterate over all files in the given directory
    for filename in os.listdir(directory):
        # Check if the filename matches the given pattern
        if regex.match(filename):
            # Construct the full file path
            file_path = os.path.join(directory, filename)
            
            # Read the CSV file into a DataFrame
            df = pd.read_csv(file_path)
            
            # Ensure the DataFrame has the required columns
            if 'Month' in df.columns and 'Sales' in df.columns:
                # Create a new figure and axis for the plot
                fig, ax = plt.subplots()
                
                # Plot the sales data
                ax.plot(df['Month'], df['Sales'], marker='o')
                
                # Set the title and labels
                ax.set_title(f'Sales Data from {filename}')
                ax.set_xlabel('Month')
                ax.set_ylabel('Sales')
                
                # Rotate x-axis labels for better readability
                plt.xticks(rotation=45)
                
                # Add the axis to the list
                axes_list.append(ax)
    
    # Return the list of Axes objects
    return axes_list