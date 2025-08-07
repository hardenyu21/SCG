import pandas as pd
import random

def task_func(product_list, categories, min_value=10, max_value=100):
    # Ensure the number of products matches the number of categories
    if len(product_list) != len(categories):
        raise ValueError("The number of products must match the number of categories.")
    
    # Generate random data for quantity sold and revenue
    data = {
        'Product': product_list,
        'Category': categories,
        'Quantity Sold': [random.randint(min_value, max_value) for _ in product_list],
        'Revenue': [random.uniform(10.0, 100.0) for _ in product_list]
    }
    
    # Calculate total revenue for each product
    data['Total Revenue'] = [q * r for q, r in zip(data['Quantity Sold'], data['Revenue'])]
    
    # Create a DataFrame from the data
    df = pd.DataFrame(data)
    
    return df

# Example usage:
product_list = ['Product A', 'Product B', 'Product C']
categories = ['Category 1', 'Category 2', 'Category 3']
sales_report = task_func(product_list, categories)
print(sales_report)