import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import pandas as pd

def task_func(df, column, bins=30, density=True, alpha=0.6, color="g", seed=None):
    # Set the random seed for reproducibility
    if seed is not None:
        np.random.seed(seed)
    
    # Extract the data from the specified column
    data = df[column]
    
    # Create the histogram
    fig, ax = plt.subplots()
    count, bins, ignored = ax.hist(data, bins=bins, density=density, alpha=alpha, color=color)
    
    # Fit a normal distribution to the data
    mu, std = norm.fit(data)
    
    # Plot the normal distribution curve
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    ax.plot(x, p, 'k', linewidth=2)
    
    # Add a title and labels
    ax.set_title(f'Histogram of {column} with Normal Distribution Fit')
    ax.set_xlabel(column)
    ax.set_ylabel('Density' if density else 'Frequency')
    
    # Show the plot
    plt.show()
    
    # Return the Axes object
    return ax