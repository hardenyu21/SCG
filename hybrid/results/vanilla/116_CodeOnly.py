import numpy as np
import matplotlib.pyplot as plt

def task_func(mu, sigma, sample_size):
    # Generate random samples from a normal distribution
    samples = np.random.normal(mu, sigma, sample_size)
    
    # Plot the histogram of the generated samples
    plt.hist(samples, bins=30, alpha=0.75, color='blue')
    plt.xlabel('Sample values')
    plt.ylabel('Frequency')
    plt.title('Histogram of Generated Samples')
    plt.show()
    
    # Return the generated samples as a numpy array
    return samples