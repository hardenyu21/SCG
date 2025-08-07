import pandas as pd
import matplotlib.pyplot as plt

def task_func(data):
    # Combine the list of dictionaries into a DataFrame
    df = pd.DataFrame(data)
    
    # Fill NA/NaN values with 0
    df_filled = df.fillna(0)
    
    # Set the index to be the time column
    df_filled.set_index('Time', inplace=True)
    
    # Plot the data
    ax = df_filled.plot(kind='line', title='Fruit Sales over Time')
    
    # Set the labels for the axes
    ax.set_xlabel('Time')
    ax.set_ylabel('Sales Quantity')
    
    # Show the plot
    plt.show()
    
    # Return the Axes object
    return ax