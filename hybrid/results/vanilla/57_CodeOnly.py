import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def task_func(csv_file_path: str, title: str):
    # Load the data from the CSV file into a DataFrame
    df = pd.read_csv(csv_file_path)
    
    # Calculate the correlation matrix and round each value to 2 decimals
    corr_df = df.corr().round(2)
    
    # Create a heatmap using seaborn
    plt.figure(figsize=(10, 8))
    ax = sns.heatmap(corr_df, annot=True, cmap='coolwarm', cbar=True, square=True, fmt='.2f')
    
    # Set the title of the heatmap
    ax.set_title(title, fontsize=16)
    
    # Display the heatmap
    plt.show()
    
    # Return the correlation DataFrame and the Axes object
    return corr_df, ax