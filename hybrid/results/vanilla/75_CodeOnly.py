import pandas as pd
import numpy as np
import itertools
from datetime import datetime, timedelta
import seaborn as sns

def task_func(df, fruits=None, days=None, seed=None, sales_lower_bound=1, sales_upper_bound=50):
    # Validate input DataFrame
    if not isinstance(df, pd.DataFrame):
        raise TypeError("The 'df' parameter must be a pandas DataFrame.")
    if not df.empty:
        raise ValueError("The 'df' parameter must be an empty DataFrame.")
    
    # Validate sales bounds
    if sales_lower_bound >= sales_upper_bound:
        raise ValueError("The 'sales_lower_bound' must be less than 'sales_upper_bound'.")
    
    # Set random seed for reproducibility
    if seed is not None:
        np.random.seed(seed)
    
    # Generate date range
    if days is None:
        days = 30  # Default to 30 days if not specified
    start_date = datetime.now()
    date_range = [start_date + timedelta(days=i) for i in range(days)]
    
    # Generate sales data
    if fruits is None:
        fruits = ['Apple', 'Banana', 'Cherry']  # Default fruits if not specified
    sales_data = []
    
    for date, fruit in itertools.product(date_range, fruits):
        sales = np.random.randint(sales_lower_bound, sales_upper_bound + 1)
        sales_data.append({'Date': date, 'Fruit': fruit, 'Sales': sales})
    
    # Create DataFrame from sales data
    sales_df = pd.DataFrame(sales_data)
    
    # Append sales data to the input DataFrame
    updated_df = pd.concat([df, sales_df], ignore_index=True)
    
    # Create a seaborn boxplot
    plt.figure(figsize=(10, 6))
    boxplot = sns.boxplot(x='Fruit', y='Sales', data=updated_df)
    plt.title('Sales Distribution by Fruit')
    plt.xlabel('Fruit')
    plt.ylabel('Sales')
    
    # Return the updated DataFrame and the boxplot
    return updated_df, boxplot