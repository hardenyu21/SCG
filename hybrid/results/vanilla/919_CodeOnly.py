import pandas as pd
import matplotlib.pyplot as plt

def task_func(data, column):
    # Define the categories
    CATEGORIES = ['A', 'B', 'C', 'D', 'E']
    
    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(data)
    
    # Count the occurrences of each category in the specified column
    category_counts = df[column].value_counts().reindex(CATEGORIES, fill_value=0)
    
    # Create a bar chart
    fig, ax = plt.subplots()
    category_counts.plot(kind='bar', ax=ax)
    
    # Set the labels and title
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')
    ax.set_title(f'Distribution of {column}')
    
    # Return the Axes object
    return ax