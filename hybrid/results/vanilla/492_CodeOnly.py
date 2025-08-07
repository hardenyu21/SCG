import pandas as pd
from datetime import datetime, timedelta
import random

def task_func(
    epoch_milliseconds,
    random_seed=0,
    products=["Product1", "Product2", "Product3", "Product4", "Product5"],
):
    # Check input validity
    if not isinstance(epoch_milliseconds, int) or epoch_milliseconds < 0:
        raise ValueError("epoch_milliseconds must be a non-negative integer.")
    
    if not isinstance(random_seed, int):
        raise ValueError("random_seed must be an integer.")
    
    if not isinstance(products, list) or not all(isinstance(p, str) for p in products):
        raise ValueError("products must be a list of strings.")
    
    # Set the random seed for reproducibility
    random.seed(random_seed)
    
    # Convert epoch milliseconds to datetime
    start_date = datetime.fromtimestamp(epoch_milliseconds / 1000.0)
    end_date = datetime.now()
    
    # Generate a list of dates from start_date to end_date
    date_list = [start_date + timedelta(days=x) for x in range((end_date - start_date).days + 1)]
    
    # Prepare a list to store sales data
    sales_data = []
    
    # Generate random sales data for each product and date
    for date in date_list:
        for product in products:
            sales = random.randint(10, 50)
            sales_data.append({'Product': product, 'Date': date, 'Sales': sales})
    
    # Create a DataFrame from the sales data
    df = pd.DataFrame(sales_data)
    
    return df