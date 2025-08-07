import random
import matplotlib.pyplot as plt
import numpy as np

# Constants
DISTRIBUTION_SIZE = 1000

def task_func(bins=30):
    # Generate a Gaussian distribution
    distribution = [random.gauss(0, 1) for _ in range(DISTRIBUTION_SIZE)]
    
    # Plot the histogram
    fig, ax = plt.subplots()
    ax.hist(distribution, bins=bins, density=True, alpha=0.75, color='blue')
    
    # Plot the Gaussian function for comparison
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = np.exp(-((x - 0) ** 2) / (2 * 1 ** 2)) / (1 * np.sqrt(2 * np.pi))
    ax.plot(x, p, 'k', linewidth=2)
    
    # Set labels and title
    ax.set_title('Gaussian Distribution Histogram')
    ax.set_xlabel('Value')
    ax.set_ylabel('Density')
    
    # Show the plot
    plt.show()
    
    # Return the distribution and the Axes object
    return distribution, ax

# Example usage
distribution, ax = task_func()