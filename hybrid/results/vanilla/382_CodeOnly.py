import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

def task_func(length):
    # Constants for the normal distribution
    MU = 0
    SIGMA = 1
    
    # Generate a normal distribution with the given length
    distribution = np.random.normal(loc=MU, scale=SIGMA, size=length)
    
    # Create a histogram of the distribution
    fig, ax = plt.subplots()
    count, bins, ignored = ax.hist(distribution, bins=30, density=True, alpha=0.6, color='g', label='Histogram')
    
    # Plot the probability density function
    pdf_x = np.linspace(min(bins), max(bins), 1000)
    pdf_y = norm.pdf(pdf_x, MU, SIGMA)
    ax.plot(pdf_x, pdf_y, 'k', linewidth=2, label='PDF')
    
    # Add labels and legend
    ax.set_title('Normal Distribution')
    ax.set_xlabel('Value')
    ax.set_ylabel('Density')
    ax.legend()
    
    # Return the distribution and the plot
    return distribution, ax

# Example usage:
# distribution, ax = task_func(1000)
# plt.show()