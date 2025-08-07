import pandas as pd
import numpy as np
import random
from random import randint, seed

# Constants
CATEGORIES = ['Electronics', 'Clothing', 'Home & Kitchen', 'Books', 'Toys & Games']

def task_func(mystrings, n_products, seed=0):
    # Set the random seed for reproducibility
    random.seed(seed)
    np.random.seed(seed)
    
    # Generate product names with spaces replaced by underscores
    product_names = [name.replace(' ', '_') for name in mystrings]
    
    # Ensure we have enough product names or truncate if necessary
    if len(product_names) > n_products:
        product_names = product_names[:n_products]
    else:
        # If not enough product names, repeat them
        product_names = (product_names * (n_products // len(product_names) + 1))[:n_products]
    
    # Randomly assign categories to each product
    categories = [random.choice(CATEGORIES) for _ in range(n_products)]
    
    # Generate prices based on a normal distribution
    prices = np.random.normal(loc=50, scale=10, size=n_products).round(2)
    
    # Create a DataFrame
    product_catalog = pd.DataFrame({
        'Product Name': product_names,
        'Category': categories,
        'Price': prices
    })
    
    return product_catalog

# Example usage:
# mystrings = ['Laptop', 'T-shirt', 'Blender', 'Novel', 'Toy Car']
# n_products = 10
# print(task_func(mystrings, n_products))