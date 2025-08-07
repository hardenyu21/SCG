import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def task_func(mu, sigma, sample_size, seed=0):
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Generate a random sample from a normal distribution
    sample = np.random.normal(loc=mu, scale=sigma, size=sample_size)
    
    # Create a Gaussian kernel density estimate
    kde = stats.gaussian_kde(sample)
    
    # Define the range for the x-axis
    x = np.linspace(min(sample), max(sample), 1000)
    
    # Plot the KDE
    fig, ax = plt.subplots()
    ax.plot(x, kde(x), label='KDE')
    
    # Plot the original normal distribution for comparison
    ax.plot(x, stats.norm.pdf(x, mu, sigma), label='True Distribution', linestyle='--')
    
    # Add labels and legend
    ax.set_xlabel('Value')
    ax.set_ylabel('Density')
    ax.legend()
    
    # Return the Axes object
    return ax

# Example usage:
# ax = task_func(mu=0, sigma=1, sample_size=1000)
# plt.show()