import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def task_func(n_samples=1000, mu=0, sigma=1, random_seed=0):
    # Set the random seed for reproducibility
    np.random.seed(random_seed)
    
    # Generate samples from a normal distribution
    samples = np.random.normal(loc=mu, scale=sigma, size=n_samples)
    
    # Create a figure and axis for plotting
    fig, ax = plt.subplots()
    
    # Plot the histogram of the samples with density normalization
    ax.hist(samples, bins=30, density=True, alpha=0.6, color='g', edgecolor='black')
    
    # Calculate the PDF values for the range of the samples
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, sigma)
    
    # Plot the PDF as a red line
    ax.plot(x, p, 'r-', linewidth=2)
    
    # Set labels and title
    ax.set_title('Histogram and PDF of Normal Distribution')
    ax.set_xlabel('Value')
    ax.set_ylabel('Density')
    
    # Show the plot
    plt.show()
    
    # Return the Axes object and the samples
    return ax, samples

# Example usage
ax, samples = task_func(n_samples=1000, mu=0, sigma=1, random_seed=42)