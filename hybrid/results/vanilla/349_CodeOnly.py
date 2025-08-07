import pandas as pd
import random

def task_func(product_list, categories):
    # Ensure the number of products matches the number of categories
    if len(product_list) != len(categories):
        raise ValueError("The number of products must match the number of categories.")
    
    # Initialize lists to store sales data
    quantity_sold = []
    revenue = []
    
    # Generate random sales data for each product
    for _ in product_list:
        q_sold = random.randint(1, 100)
        price_per_unit = random.randint(10, 100)
        r_generated = q_sold * price_per_unit
        
        quantity_sold.append(q_sold)
        revenue.append(r_generated)
    
    # Create a DataFrame with the sales data
    sales_data = {
        'Product': product_list,
        'Category': categories,
        'Quantity Sold': quantity_sold,
        'Revenue': revenue
    }
    
    df = pd.DataFrame(sales_data)
    
    return df

# Example usage:
product_list = ['Product A', 'Product B', 'Product C']
categories = ['Category 1', 'Category 2', 'Category 3']
sales_report = task_func(product_list, categories)
print(sales_report)