from random import randint
from statistics import mean
import pandas as pd

def task_func(products_list):
    # Initialize a list to store the sales data for each product
    sales_data = []

    # Iterate over each product in the list
    for product in products_list:
        # Generate random sales data for 12 months
        monthly_sales = [randint(100, 1000) for _ in range(12)]
        
        # Calculate the average sales for the product
        average_sales = mean(monthly_sales)
        
        # Append the product name, monthly sales, and average sales to the sales_data list
        sales_data.append([product] + monthly_sales + [average_sales])

    # Define the column names for the DataFrame
    columns = ['Product'] + [f'Month {i+1}' for i in range(12)] + ['Average Sales']
    
    # Create a pandas DataFrame from the sales data
    df = pd.DataFrame(sales_data, columns=columns)
    
    return df

# Example usage:
# products = ['Product A', 'Product B', 'Product C']
# df = task_func(products)
# print(df)