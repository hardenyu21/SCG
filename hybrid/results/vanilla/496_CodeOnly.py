from datetime import datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt

def task_func(days_in_past=7, random_seed=0):
    if days_in_past < 1:
        raise ValueError("days_in_past must be at least 1.")
    
    # Set the random seed for reproducibility
    np.random.seed(random_seed)
    
    # Generate random temperatures between 15 and 35
    temperatures = np.random.randint(15, 36, size=days_in_past)
    
    # Generate dates for the past week
    dates = [datetime.now() - timedelta(days=i) for i in range(days_in_past)]
    dates.reverse()  # Reverse to have the oldest date first
    
    # Create the plot
    fig, ax = plt.subplots()
    ax.plot(dates, temperatures, marker='o', linestyle='-')
    
    # Set labels and title
    ax.set_xlabel('Date')
    ax.set_ylabel('Temperature (°C)')
    ax.set_title('Temperature Trend')
    
    # Format the x-axis to show dates
    fig.autofmt_xdate()
    
    # Show the plot
    plt.show()
    
    return ax

# Example usage
task_func()