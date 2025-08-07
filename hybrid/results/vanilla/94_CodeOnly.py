import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

def task_func(mean, std_dev, num_samples):
    # Generate samples from a normal distribution
    samples = np.random.normal(loc=mean, scale=std_dev, size=num_samples)
    
    # Create a histogram of the samples
    fig, ax = plt.subplots()
    count, bins, ignored = ax.hist(samples, bins=30, density=True, alpha=0.6, color='g', edgecolor='black')
    
    # Overlay the PDF of the normal distribution
    pdf_x = np.linspace(min(bins), max(bins), 1000)
    pdf_y = norm.pdf(pdf_x, mean, std_dev)
    ax.plot(pdf_x, pdf_y, 'k', linewidth=2)
    
    # Set the title with the fit results
    ax.set_title(f"Fit results: mean = {mean:.2f}, std = {std_dev:.2f}")
    
    # Show the plot
    plt.show()
    
    # Return the figure and the samples
    return fig, samples

# Example usage:
# fig, samples = task_func(0, 1, 1000)