import pandas as pd
import matplotlib.pyplot as plt

def task_func(csv_file_path, col1_name="column1", col2_name="column2"):
    # Read data from the CSV file
    df = pd.read_csv(csv_file_path)
    
    # Group the DataFrame by 'col1_name' and calculate the mean of 'col2_name' for each group
    grouped_mean = df.groupby(col1_name)[col2_name].mean()
    
    # Create a bar plot
    fig, ax = plt.subplots()
    grouped_mean.plot(kind='bar', ax=ax)
    
    # Set the title and labels
    ax.set_title(f"Mean of {col2_name} Grouped by {col1_name}")
    ax.set_xlabel(col1_name)
    ax.set_ylabel(f"Mean of {col2_name}")
    
    # Return the Axes object for further customization
    return ax