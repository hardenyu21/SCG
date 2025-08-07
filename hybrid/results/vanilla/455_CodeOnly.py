import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def task_func(mean, std_dev, n):
    # Generate samples from a normal distribution
    samples = np.random.normal(loc=mean, scale=std_dev, size=n)
    
    # Plot histogram of the samples
    plt.hist(samples, bins=30, density=True, alpha=0.6, color='g', label='Histogram of samples')
    
    # Plot the probability density function
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = stats.norm.pdf(x, mean, std_dev)
    plt.plot(x, p, 'k', linewidth=2, label='PDF')
    
    # Add labels and legend
    plt.title('Histogram and PDF of Generated Samples')
    plt.xlabel('Value')
    plt.ylabel('Density')
    plt.legend()
    
    # Show the plot
    plt.show()
    
    return samples

# Example usage
samples = task_func(5, 2, 500)
print(len(samples))  # Should output 500