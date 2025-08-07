import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def task_func(mu, sigma, num_samples=1000, seed=77):
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Generate samples from a normal distribution
    samples = np.random.normal(loc=mu, scale=sigma, size=num_samples)
    
    # Create a figure with two subplots
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    
    # Plot the histogram
    axes[0].hist(samples, bins=30, density=True, alpha=0.6, color='g', edgecolor='black')
    axes[0].set_title('Histogram')
    axes[0].set_xlabel('Value')
    axes[0].set_ylabel('Density')
    
    # Plot the Q-Q plot
    stats.probplot(samples, dist="norm", plot=axes[1])
    axes[1].set_title('Q-Q Plot')
    
    # Adjust layout
    plt.tight_layout()
    
    # Return the figure
    return fig

# Example usage:
# fig = task_func(mu=0, sigma=1)
# plt.show()