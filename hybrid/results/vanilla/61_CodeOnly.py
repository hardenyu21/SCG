import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# Constants
PLOT_TITLE = 'Square root plot'
X_LABEL = 'x'
Y_LABEL = 'sqrt(x)'
TIME_FORMAT = '%Y-%m-%d %H:%M:%S'

def task_func(result):
    # Extract values associated with the key 'from_user'
    x_values = [d['from_user'] for d in result if 'from_user' in d]
    
    # Calculate square root values and round them to 2 decimals
    sqrt_values = np.round(np.sqrt(x_values), 2)
    
    # Create the plot
    fig, ax = plt.subplots()
    ax.plot(x_values, sqrt_values, marker='o')
    
    # Annotate the plot with the current date and time
    current_time = datetime.now().strftime(TIME_FORMAT)
    ax.annotate(f'Generated on: {current_time}', xy=(0.05, 0.95), xycoords='axes fraction',
                fontsize=10, ha='left', va='top', bbox=dict(boxstyle="round,pad=0.3", edgecolor='black', facecolor='white'))
    
    # Set plot title and labels
    ax.set_title(PLOT_TITLE)
    ax.set_xlabel(X_LABEL)
    ax.set_ylabel(Y_LABEL)
    
    # Show the plot
    plt.grid(True)
    plt.show()
    
    # Return the square root values as a numpy array and the plot axes
    return sqrt_values, ax