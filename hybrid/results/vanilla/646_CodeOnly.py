import os
import pandas as pd
from dateutil.parser import parse
import matplotlib.pyplot as plt

OUTPUT_DIR = './output'

def task_func(csv_path=os.path.join(OUTPUT_DIR, 'data.csv'), date_column='date'):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_path)
    
    # Convert the date column to datetime objects
    df[date_column] = df[date_column].apply(parse)
    
    # Extract the year from the datetime objects
    df['year'] = df[date_column].dt.year
    
    # Plot the histogram of the year distribution
    fig, ax = plt.subplots()
    ax.hist(df['year'], bins=range(df['year'].min(), df['year'].max() + 2), edgecolor='black')
    
    # Set labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Frequency')
    ax.set_title('Year Distribution of Dates')
    
    # Show the plot
    plt.show()
    
    return ax

# Example usage:
# ax = task_func(csv_path='path_to_your_csv_file.csv', date_column='your_date_column_name')