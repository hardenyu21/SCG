import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Constants
START_DATE = '2016-01-01'
PERIODS = 13
FREQ = 'WOM-2FRI'
CATEGORIES = ['Electronics', 'Fashion', 'Home & Kitchen', 'Automotive', 'Sports']

def task_func(start_date=START_DATE, periods=PERIODS, freq=FREQ, categories=CATEGORIES):
    # Generate a date range
    dates = pd.date_range(start=start_date, periods=periods, freq=freq)
    
    # Create a DataFrame to hold the sales data
    sales_data = []
    
    for date in dates:
        for category in categories:
            # Generate random sales data
            sales = np.random.randint(100, 1000)
            sales_data.append({'Date': date, 'Category': category, 'Sales': sales})
    
    # Create a DataFrame from the sales data
    df = pd.DataFrame(sales_data)
    
    # Plotting
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Plot sales for each category
    for category in categories:
        category_data = df[df['Category'] == category]
        ax.plot(category_data['Date'], category_data['Sales'], label=category, marker='o')
    
    # Set plot title and labels
    ax.set_title('Sales Report by Category')
    ax.set_xlabel('Date')
    ax.set_ylabel('Sales')
    ax.legend(title='Category')
    ax.grid(True)
    
    # Rotate date labels for better readability
    plt.xticks(rotation=45)
    
    # Show plot
    plt.tight_layout()
    plt.show()
    
    return df, ax

# Example usage
df, ax = task_func()