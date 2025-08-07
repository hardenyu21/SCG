import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

def task_func(start_date, end_date, seed=42):
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Convert start and end dates to datetime objects
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    
    # Generate a list of dates from start_date to end_date, inclusive
    date_range = [start_date + timedelta(days=x) for x in range((end_date - start_date).days + 1)]
    
    # Generate random sales data for each date
    sales_data = np.random.randint(0, 501, size=len(date_range))
    
    # Create a DataFrame with the date and sales data
    df = pd.DataFrame({'Date': date_range, 'Sales': sales_data})
    
    # Plot the sales data over time
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df['Date'], df['Sales'], marker='o', linestyle='-')
    ax.set_title('Sales Over Time')
    ax.set_xlabel('Date')
    ax.set_ylabel('Sales')
    ax.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Return the DataFrame and the Axes object
    return df, ax

# Example usage:
# df, ax = task_func('2023-01-01', '2023-01-10')
# plt.show()