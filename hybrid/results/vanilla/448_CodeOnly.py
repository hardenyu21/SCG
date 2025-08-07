import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def task_func(mu=0, sigma=1):
    # Create an array of 100 linearly spaced numbers between mu - 3*sigma and mu + 3*sigma
    x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
    
    # Calculate the normal distribution values
    y = norm.pdf(x, mu, sigma)
    
    # Create a subplot
    fig, ax = plt.subplots()
    
    # Plot the normal distribution
    ax.plot(x, y, label=f'Normal Distribution (μ={mu}, σ={sigma})')
    
    # Add labels and title
    ax.set_xlabel('x')
    ax.set_ylabel('Probability Density')
    ax.set_title('Normal Distribution')
    
    # Add a legend
    ax.legend()
    
    # Show the plot
    plt.show()
    
    # Return the Axes object
    return ax

# Example usage:
# ax = task_func(mu=0, sigma=1)