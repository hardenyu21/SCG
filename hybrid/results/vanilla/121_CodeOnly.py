import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(my_list, seed=42):
    # Check if my_list is a list
    if not isinstance(my_list, list):
        raise TypeError("my_list must be a list.")
    
    # Add item "12" to the list
    my_list.append("12")
    
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Define the categories
    categories = ['Electronics', 'Fashion', 'Home & Kitchen', 'Automotive', 'Sports']
    
    # Generate random sales data for each category
    sales_data = np.random.randint(1000, 10000, size=len(categories))
    
    # Create a DataFrame with the sales data
    df_sales = pd.DataFrame({
        'Category': categories,
        'Sales': sales_data
    })
    
    # Plot the sales data
    fig, ax = plt.subplots()
    df_sales.plot(kind='bar', x='Category', y='Sales', ax=ax, legend=False)
    ax.set_ylabel('Sales')
    ax.set_title('Simulated Sales Data')
    
    # Return the DataFrame and the Axes object
    return df_sales, ax

# Example usage:
# my_list = []
# df, ax = task_func(my_list)
# plt.show()