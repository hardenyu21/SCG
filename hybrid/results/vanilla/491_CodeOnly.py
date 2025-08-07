import random
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

def task_func(epoch_milliseconds, seed=None):
    # Set the random seed for reproducibility
    if seed is not None:
        random.seed(seed)
    
    # Convert epoch milliseconds to a datetime object
    start_date = datetime.utcfromtimestamp(epoch_milliseconds / 1000.0)
    current_date = datetime.utcnow()
    
    # Validate the start date
    if epoch_milliseconds < 0 or start_date > current_date:
        raise ValueError("The start time is negative or after the current time.")
    
    # Calculate the number of days between the start date and the current date
    num_days = (current_date - start_date).days + 1
    
    # Define the categories
    categories = ['Electronics', 'Clothing', 'Home', 'Books', 'Sports']
    
    # Initialize sales data
    sales_data = {category: [] for category in categories}
    
    # Generate random sales data for each day
    for day in range(num_days):
        for category in categories:
            sales = random.randint(10, 50)
            sales_data[category].append(sales)
    
    # Plot the sales trend
    fig, ax = plt.subplots(figsize=(10, 6))
    for category in categories:
        ax.plot(range(num_days), sales_data[category], label=category)
    
    ax.set_xlabel('Days since ({})'.format(start_date.strftime('%Y-%m-%d')))
    ax.set_ylabel('Sales Units')
    ax.set_title('Sales Trend Over Time')
    ax.legend()
    ax.grid(True)
    
    # Show the plot
    plt.show()
    
    return sales_data, ax

# Example usage:
# epoch_milliseconds = 1609459200000  # Example epoch milliseconds for January 1, 2021
# sales_data, ax = task_func(epoch_milliseconds, seed=42)