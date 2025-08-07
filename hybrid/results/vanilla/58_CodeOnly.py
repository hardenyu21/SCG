import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def task_func(mu, sigma, num_samples):
    # Generate random samples from a normal distribution
    samples = np.random.normal(mu, sigma, num_samples)
    
    # Create a figure and axis
    fig, ax = plt.subplots()
    
    # Plot the histogram of the samples
    ax.hist(samples, bins=30, density=True, alpha=0.6, color='g', label='Histogram of samples')
    
    # Plot the normal distribution curve
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = stats.norm.pdf(x, mu, sigma)
    ax.plot(x, p, 'k', linewidth=2, label='Normal distribution')
    
    # Add labels and title
    ax.set_title('Normal Distribution')
    ax.set_xlabel('Value')
    ax.set_ylabel('Density')
    
    # Add legend
    ax.legend()
    
    # Show the plot
    plt.show()
    
    # Return the figure for testing purposes
    return fig