import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(data):
    # Convert string prices to float, handling commas as thousand separators
    data['Price'] = data['Price_String'].str.replace(',', '').astype(float)
    
    # Calculate statistical measures
    mean_price = data['Price'].mean()
    median_price = data['Price'].median()
    std_dev_price = data['Price'].std()
    
    # Create a dictionary with the calculated statistics
    stats = {
        'mean': mean_price,
        'median': median_price,
        'std_dev': std_dev_price
    }
    
    # Plot the histogram
    fig, ax = plt.subplots()
    ax.hist(data['Price'], bins='auto', color='blue', alpha=0.7, rwidth=0.85)
    ax.set_title('Histogram of Product Prices')
    ax.set_xlabel('Price')
    ax.set_ylabel('Frequency')
    
    # Return the statistics and the Axes object
    return stats, ax

# Example usage:
# data = pd.DataFrame({
#     'Product': ['Product A', 'Product B', 'Product C', 'Product D'],
#     'Price_String': ['1,200', '1,500', '1,800', '2,100']
# })
# stats, ax = task_func(data)
# plt.show()