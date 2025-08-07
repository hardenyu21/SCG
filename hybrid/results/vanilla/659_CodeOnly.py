import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

def task_func(x, y, labels):
    # Check if the input arrays and labels have the same length
    if not (len(x) == len(y) == len(labels)):
        raise ValueError("The length of x, y, and labels must be the same.")
    
    # Create a figure and axis
    fig, ax = plt.subplots()
    
    # Plot normal distributions for each pair (x, y) with corresponding label
    for i in range(len(x)):
        # Calculate the mean and standard deviation
        mean = x[i]
        std_dev = y[i]
        
        # Generate a range of x values for the normal distribution
        x_values = np.linspace(mean - 4*std_dev, mean + 4*std_dev, 1000)
        
        # Calculate the normal distribution
        y_values = stats.norm.pdf(x_values, mean, std_dev)
        
        # Plot the normal distribution
        ax.plot(x_values, y_values, label=labels[i])
    
    # Add labels and legend
    ax.set_xlabel('Value')
    ax.set_ylabel('Probability Density')
    ax.set_title('Normal Distributions of Chemical Compounds')
    ax.legend()
    
    # Show the plot
    plt.show()
    
    # Return the figure object
    return fig