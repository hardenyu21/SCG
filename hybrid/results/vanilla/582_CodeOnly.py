import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def task_func(size=1000):
    # Generate normally distributed random numbers
    data = np.random.normal(loc=0, scale=1, size=size)
    
    # Create a figure and axis
    fig, ax = plt.subplots()
    
    # Plot the histogram of the data
    count, bins, ignored = ax.hist(data, bins=30, density=True, alpha=0.6, color='g', label='Histogram')
    
    # Plot the PDF of the normal distribution
    pdf_x = np.linspace(min(bins), max(bins), 1000)
    pdf_y = stats.norm.pdf(pdf_x, loc=0, scale=1)
    ax.plot(pdf_x, pdf_y, 'k', linewidth=2, label='PDF')
    
    # Add labels and legend
    ax.set_title('Histogram and PDF of Normally Distributed Random Numbers')
    ax.set_xlabel('Value')
    ax.set_ylabel('Density')
    ax.legend()
    
    # Return the figure object
    return fig

# Example usage:
# fig = task_func()
# plt.show()