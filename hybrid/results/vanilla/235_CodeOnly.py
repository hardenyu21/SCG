import numpy as np
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
from scipy.stats import norm

def task_func(mu, sigma, seed=0, num_samples=1000, num_bins=30):
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Generate random samples from a normal distribution
    samples = np.random.normal(mu, sigma, num_samples)
    
    # Create a histogram of the samples
    fig, ax = plt.subplots()
    count, bins, ignored = ax.hist(samples, bins=num_bins, density=True, alpha=0.6, color='b', edgecolor='black')
    
    # Calculate the PDF of the normal distribution
    pdf_x = np.linspace(min(bins), max(bins), 1000)
    pdf_y = norm.pdf(pdf_x, mu, sigma)
    
    # Overlay the PDF on the histogram
    ax.plot(pdf_x, pdf_y, 'r-', linewidth=2, label='PDF')
    
    # Fit a second order polynomial to the histogram bins using OLS
    bin_centers = 0.5 * (bins[:-1] + bins[1:])
    model = ols('count ~ I(bin_centers**2) + bin_centers', data={'count': count, 'bin_centers': bin_centers}).fit()
    
    # Generate the polynomial values
    poly_x = np.linspace(min(bins), max(bins), 1000)
    poly_y = model.predict({'bin_centers': poly_x, 'I(bin_centers**2)': poly_x**2})
    
    # Overlay the polynomial on the histogram
    ax.plot(poly_x, poly_y, 'g-', linewidth=2, label='2nd Order Polynomial')
    
    # Add labels and legend
    ax.set_xlabel('Value')
    ax.set_ylabel('Density')
    ax.legend()
    
    # Show the plot
    plt.show()
    
    return ax

# Example usage:
# ax = task_func(mu=0, sigma=1)