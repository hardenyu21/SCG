import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def task_func(mu=0, sigma=1, sample_size=1000, seed=0):
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Generate a sample from a normal distribution
    sample = np.random.normal(loc=mu, scale=sigma, size=sample_size)
    
    # Calculate the empirical mean and standard deviation
    empirical_mean = np.mean(sample)
    empirical_std = np.std(sample, ddof=1)  # Using Bessel's correction
    
    # Create a histogram of the sample
    fig, ax = plt.subplots()
    count, bins, ignored = ax.hist(sample, bins=30, density=True, alpha=0.6, color='g', edgecolor='black')
    
    # Plot the probability density function (PDF)
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = stats.norm.pdf(x, mu, sigma)
    ax.plot(x, p, 'k', linewidth=2)
    
    # Set the title with the given format
    ax.set_title(r'Normal Distribution with $\mu = %0.2f, \sigma = %0.2f$' % (mu, sigma))
    
    # Return the Axes object and the empirical mean and standard deviation
    return ax, empirical_mean, empirical_std

# Example usage:
# ax, empirical_mean, empirical_std = task_func(mu=5, sigma=2, sample_size=1000, seed=42)
# plt.show()
# print("Empirical Mean:", empirical_mean)
# print("Empirical Standard Deviation:", empirical_std)