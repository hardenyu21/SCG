import pandas as pd
from random import randint, uniform, seed

def task_func(categories=None, months=None, random_seed=42):
    # Validate input
    if not isinstance(categories, list) or not categories:
        raise ValueError("The 'categories' parameter must be a non-empty list.")
    if not isinstance(months, list) or not months:
        raise ValueError("The 'months' parameter must be a non-empty list.")
    
    # Set the random seed for reproducibility
    seed(random_seed)
    
    # Initialize lists to store data
    all_months = []
    all_categories = []
    all_sales = []
    
    # Generate sales data for each category and month
    for month in months:
        for category in categories:
            # Generate a random sales value
            sales = randint(100, 500) + uniform(0, 1)
            # Append data to lists
            all_months.append(month)
            all_categories.append(category)
            all_sales.append(sales)
    
    # Create a DataFrame
    df = pd.DataFrame({
        'Month': all_months,
        'Category': all_categories,
        'Sales': all_sales
    })
    
    return df