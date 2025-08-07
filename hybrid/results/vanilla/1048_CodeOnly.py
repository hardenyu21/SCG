from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

def task_func(date_str):
    # Parse the date string to a datetime object
    date = datetime.strptime(date_str, '%Y-%m-%d')
    
    # Extract the day of the month
    day_of_month = date.day
    
    # Define the frequency of the sine wave based on the day of the month
    frequency = day_of_month
    
    # Generate x values from 0 to 2*pi
    x = np.linspace(0, 2 * np.pi, 1000)
    
    # Calculate the y values for the sine wave
    y = np.sin(frequency * x)
    
    # Create a plot
    fig, ax = plt.subplots()
    ax.plot(x, y)
    
    # Set the title and labels
    ax.set_title(f'Sine Wave with Frequency {frequency} (Day of Month: {day_of_month})')
    ax.set_xlabel('x')
    ax.set_ylabel('sin(frequency * x)')
    
    # Show the grid
    ax.grid(True)
    
    # Return the Axes object
    return ax

# Example usage:
# ax = task_func('2023-10-15')
# plt.show()