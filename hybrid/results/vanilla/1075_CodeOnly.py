import datetime
import numpy as np
import matplotlib.pyplot as plt

# Constants
TIME_FORMAT = "%d/%m/%y %H:%M:%S.%f"

def task_func(time_strings):
    # Convert datetime strings to datetime objects
    datetimes = [datetime.datetime.strptime(ts, TIME_FORMAT) for ts in time_strings]
    
    # Calculate differences in seconds between consecutive datetime objects
    differences = [int((datetimes[i+1] - datetimes[i]).total_seconds()) for i in range(len(datetimes) - 1)]
    
    # Plot the differences as a bar chart
    fig, ax = plt.subplots()
    ax.bar(range(len(differences)), differences)
    
    # Set labels and title
    ax.set_xlabel('Consecutive Pairs')
    ax.set_ylabel('Difference in Seconds')
    ax.set_title('Differences in Seconds Between Consecutive Datetimes')
    
    # Show the plot
    plt.show()
    
    # Return the axes object for further customization
    return ax