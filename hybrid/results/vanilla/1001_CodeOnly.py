import pandas as pd
import matplotlib.pyplot as plt

def task_func(csv_file_path: str):
    # Read data from the CSV file
    data = pd.read_csv(csv_file_path)
    
    # Normalize the 'column1' data
    column1 = data['column1']
    normalized_column1 = (column1 - column1.min()) / (column1.max() - column1.min())
    
    # Create the plot
    fig, ax = plt.subplots()
    ax.plot(normalized_column1)
    
    # Set the title with formatted strings
    title = f"{'Plot Title':<20}:{'Normalized Column 1':>20}"
    ax.set_title(title)
    
    # Set the x-label with formatted strings
    xlabel = f"{'Index':<20}:{'Normalized Value':>20}"
    ax.set_xlabel(xlabel)
    
    # Set the y-label with formatted strings
    ylabel = f"{'Frequency':<20}:{'Normalized Value':>20}"
    ax.set_ylabel(ylabel)
    
    # Show the plot
    plt.show()
    
    # Return the Axes object
    return ax