import numpy as np
import pandas as pd

def task_func(products, n_samples=100, sales_lower=50, sales_upper=200, profit_margin_min=0.1, profit_margin_max=0.5, random_seed=42):
    # Validate input types and values
    if not isinstance(products, list) or not all(isinstance(p, str) for p in products):
        raise TypeError("products must be a list of strings.")
    if not isinstance(n_samples, int) or n_samples <= 0:
        raise ValueError("n_samples must be a positive integer.")
    if not isinstance(sales_lower, (int, float)) or not isinstance(sales_upper, (int, float)):
        raise TypeError("sales_lower and sales_upper must be numeric.")
    if not isinstance(profit_margin_min, (int, float)) or not isinstance(profit_margin_max, (int, float)):
        raise TypeError("profit_margin_min and profit_margin_max must be numeric.")
    if sales_lower > sales_upper:
        raise ValueError("sales_lower must not be greater than sales_upper.")
    
    # Set random seed for reproducibility
    np.random.seed(random_seed)
    
    # Generate random sales and profit data
    data = []
    for product in products:
        sales = np.random.uniform(sales_lower, sales_upper, n_samples)
        profit_margins = np.random.uniform(profit_margin_min, profit_margin_max, n_samples)
        profits = sales * profit_margins
        
        total_sales = np.sum(sales)
        total_profit = np.sum(profits)
        
        data.append({
            'Product': product,
            'Total Sales': total_sales,
            'Total Profit': total_profit
        })
    
    # Create a DataFrame from the data
    df = pd.DataFrame(data)
    
    # Sort the DataFrame by Total Profit in descending order
    df = df.sort_values(by='Total Profit', ascending=False).reset_index(drop=True)
    
    return df

# Example usage:
# products = ['Product A', 'Product B', 'Product C']
# report = task_func(products)
# print(report)